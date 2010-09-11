"""
This file is to test testmaker. It will run over the polls app and with the crawler and with test maker outputting things. Hopefully this will provide a sane way to test testmaker.
"""

import logging
import os
import shutil
import tempfile

from django.test.testcases import TestCase

from crawler.base import Crawler

class CrawlerTests(TestCase):
    """
    Tests to test the Crawler API
    """
    urls = "test_project.polls.urls"
    fixtures = ['polls_testmaker.json']

    def setUp(self):
        self.log = logging.getLogger('crawler')
        [self.log.removeHandler(h) for h in self.log.handlers]
        self.log.setLevel(logging.DEBUG)
        handler = logging.FileHandler('crawler_log', 'a')
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.log.addHandler(handler)

    def tearDown(self):
        os.remove('crawler_log')

    def test_basic_crawling(self):
        c = Crawler('/')
        c.run()
        self.assertEqual(c.crawled, {'/': True, u'/1': True, u'/2': True})

    def test_relative_crawling(self):
        c = Crawler('/1')
        c.run()
        self.assertEqual(c.crawled, {u'/1': True})

    def test_url_plugin(self):
        conf_urls = {'this_wont_be_crawled': True}
        c = Crawler('/', conf_urls=conf_urls)
        c.run()
        logs = open('crawler_log')
        output = logs.read()
        self.assertTrue(output.find('These patterns were not matched during the crawl: this_wont_be_crawled') != -1)

    def test_time_plugin(self):
        #This isn't testing much, but I can't know how long the time will take
        c = Crawler('/')
        c.run()
        logs = open('crawler_log')
        output = logs.read()
        self.assertTrue(output.find('Time taken:') != -1)

    def test_memory_plugin(self):
        from crawler.plugins.memory_plugin import Memory
        try:
            Memory.active = True
            c = Crawler('/')
            c.run()
            logs = open('crawler_log')
            output = logs.read()
            self.assertTrue(output.find('Memory consumed:') != -1)
        finally:
            # Avoid running this plugin for all of the other tests:
            Memory.active = False

    def test_heap_plugin(self):
        try:
            from crawler.plugins.heap import HeapPlugin
        except ImportError, e:
            logging.warning("Heap plugin cannot be tested due to import error: %s", e)
            return

        output_dir = tempfile.mkdtemp()
        try:
            c = Crawler('/', output_dir=output_dir)
            c.plugins.append(HeapPlugin())
            c.run()

            heap_report = os.path.join(output_dir, "heap.csv")

            self.assertTrue(os.path.exists(heap_report))

            heap_data = file(heap_report).readlines()
            self.assertNotEqual(len(heap_data), 0)
        finally:
            shutil.rmtree(output_dir)
