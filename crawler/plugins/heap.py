import csv
import logging
import os

from django.template.defaultfilters import filesizeformat

from performance_tools.memory import Heap

from base import Plugin

LOG = logging.getLogger("crawler")


class HeapPlugin(Plugin):
    """
    Calculate heap consumed before and after request
    """
    active = False

    def __init__(self):
        super(HeapPlugin, self).__init__()
        self.heap_urls = self.data['heap_urls'] = {}
        self.csv_writer = self.csv_file = None

    def set_output_dir(self, output_dir=None):
        super(HeapPlugin, self).set_output_dir(output_dir)

        if output_dir:
            self.csv_file = open(os.path.join(output_dir, 'heap.csv'), "w")
            self.csv_writer = csv.writer(self.csv_file)

    def pre_request(self, sender, **kwargs):
        url = kwargs['url']
        self.heap = Heap()

    def post_request(self, sender, **kwargs):
        url = kwargs['url']
        stats = self.heap.deltas()
        self.heap_urls[url] = stats['size']

        LOG.debug("%s: heap consumed: %s", url, filesizeformat(self.heap_urls[url]))

        if self.csv_writer:
            self.csv_writer.writerow([url, stats['size']])

    def finish_run(self, sender, **kwargs):
        "Print the most heap consumed by a view"

        if self.csv_file:
            self.csv_file.close()

        alist = sorted(self.heap_urls.iteritems(),
            key=lambda (k,v): (v,k),
            reverse=True
        )

        for url, mem in alist[:10]:
            LOG.info("%s: %s heap", url, filesizeformat(mem))


PLUGIN = HeapPlugin