from guardicore_crawler.helpers.singleton import Singleton
from guardicore_crawler.helpers.file_controller import FileController
from guardicore_crawler.helpers.logger import Logger
from guardicore_crawler.components.report_item import ReportItem

"""
    This class writes the crawler report
    TODO Should be thread safe
"""

class Report(Singleton):

# public methods
    def __init__(self,filename):
        self.file_name = filename
        f = FileController(filename,'a')
        self.logger = Logger(f)
        self.tracker_map = {}
        self.item_counter = 0
    
    def clear(self):
        self.logger.clear_log()
    
    def insert_item(self,item):

        if not issubclass(type(item),ReportItem):
            raise TypeError('item must be of type ReportItem')
            
        if not self.is_visited(item):
            self.__add_item_to_map(item.name)
            self.__write(item)
            self.item_counter += 1
            return True
        return False

    def get_num_of_items(self):
        return self.item_counter

    def is_visited(self,item):
        return self.tracker_map.get(item.name) is not None
    
# private methods
    def __write(self, item):
        self.logger.log(str(item))
    
    def __add_item_to_map(self,item):
        self.tracker_map[item] = True
    


        