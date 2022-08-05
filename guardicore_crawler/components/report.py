from guardicore_crawler.helpers.singleton import Singleton
from guardicore_crawler.helpers.file_controller import FileController
from guardicore_crawler.helpers.logger import Logger
   
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
    
    def clear(self):
        self.logger.clear_log()
    
    def is_visited(self,item):
        return self.tracker_map.get(item) is not None
    
    def insert_item(self,item):
        if not self.is_visited(item):
            self.__add_item_to_map(item)
            self.__write(item)

    def count_items(self):
        return len(self.tracker_map)
        
# private methods
    def __write(self,message):
        self.logger.log(message)
    
    def __add_item_to_map(self,item):
        self.tracker_map[item] = True
    


        