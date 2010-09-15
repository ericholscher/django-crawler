import csv
import logging
import os

from performance_tools.query_counts import QueryCounter

from base import Plugin


LOG = logging.getLogger('crawler')


class QueryCount(Plugin):
    """
    Report the number of queries used to serve a page
    """
    active = False

    def __init__(self):
        super(QueryCount, self).__init__()

        self.csv_file = self.csv_writer = None

        self.query_counts = self.data['query_counts'] = {}

    def set_output_dir(self, output_dir=None):
        super(QueryCount, self).set_output_dir(output_dir)

        if output_dir:
            self.csv_file = open(os.path.join(output_dir, 'query_counts.csv'), "w")
            self.csv_writer = csv.writer(self.csv_file)

    def pre_request(self, sender, **kwargs):
        url = kwargs['url']
        self.query_counts[url] = QueryCounter()

    def post_request(self, sender, **kwargs):
        url = kwargs['url']

        deltas = self.query_counts[url].deltas()

        for k, v in sorted(deltas.items(), reverse=True):
            if v > 50:
                log_f = LOG.critical
            elif v > 20:
                log_f = LOG.error
            elif v > 10:
                log_f = LOG.warning
            else:
                log_f = LOG.info
            log_f("%s: %s %d queries", url, k, v)

        if self.csv_writer:
            self.csv_writer.writerow((url, sum(deltas.values())))

    def finish_run(self, sender, **kwargs):
        if self.csv_file:
            self.csv_file.close()


PLUGIN = QueryCount
