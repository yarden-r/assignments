from guardicore_crawler_v2.components.report_item import ReportItem

class BrokenUrl(ReportItem):

    def __init__(self, depth, url):
        super().__init__(url)
        self.depth = depth
    
    def __str__ (self):
        return 'Broken Link, depth: {}\n\t{}'.format(self.depth, self.name)

