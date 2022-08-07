from guardicore_crawler.helpers.singleton import Singleton
from guardicore_crawler.helpers.file_controller import FileController
from guardicore_crawler.helpers.logger import Logger
from guardicore_crawler.components.report_item import ReportItem
from guardicore_crawler.helpers.thread_lock import ThreadLock
from threading import Lock
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
        self.lock = ThreadLock()
    
    def clear(self):
        self.logger.clear_log()
    
    def insert_item(self,item):

        if not issubclass(type(item),ReportItem):
            raise TypeError('item must be of type ReportItem')
        
        

        with self.lock:
            if not self.contains_name(item.name):
                self.__add_item_to_map(item.name)
                self.__write(item)
                self.item_counter += 1

    def get_num_of_items(self):
        return self.item_counter

    def contains_name(self,name):
        return self.tracker_map.get(name) is not None
    
# private methods
    def __write(self, item):
        self.logger.log(str(item))
    
    def __add_item_to_map(self,item):
        self.tracker_map[item] = True
    


        