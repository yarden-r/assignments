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
        f = FileController(filename,'a')
        self.logger = Logger(f)
        self.tracker_map = {}
        self.item_counter = 0
    
    def clear(self):
        self.logger.clear_log()
    
    def is_visited(self,item):
        
        print(type(item))
        print(issubclass(type(item),ReportItem))

        if not issubclass(type(item),ReportItem):
            raise TypeError('item must be of type ReportItem')
        return self.tracker_map.get(item.name) is not None
    
    def insert_item(self,item):

        print("the type inside method is ", type(item))
        if not issubclass(type(item),ReportItem):
            raise TypeError('item must be of type ReportItem')
            
        if not self.is_visited(item.name):
            self.__add_item_to_map(item.name)
            self.__write(item)
            self.item_counter += 1

    def get_num_of_items(self):
        return self.item_counter

# private methods
    def __write(self,message):
        self.logger.log(message)
    
    def __add_item_to_map(self,item):
        self.tracker_map[item] = True
    


        