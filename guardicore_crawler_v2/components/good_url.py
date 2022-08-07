from guardicore_crawler_v2.components.report_item import ReportItem

class GoodUrl(ReportItem):
    """
        This class is to add a good url to the report.
    """
    def __init__(self, depth, url, text):
        super().__init__(url)
        self.text = text
        self.depth = depth
    
    def __str__ (self):
        return 'Good Link, depth: {}\n\t{}\n\t{}'.format(self.depth, self.name, self.text)

