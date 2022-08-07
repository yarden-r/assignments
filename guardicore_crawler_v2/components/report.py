from guardicore_crawler_v2.helpers.singleton import Singleton
from guardicore_crawler_v2.helpers.file_controller import FileController
from guardicore_crawler_v2.helpers.logger import Logger
from guardicore_crawler_v2.components.report_item import ReportItem
from guardicore_crawler_v2.helpers.thread_lock import ThreadLock
from guardicore_crawler_v2.helpers.unique_map import UniqueMap
"""
    This class writes the crawler report
"""

class Report(Singleton):

# public methods
    def __init__(self,filename):
        self.file_name = filename
        f = FileController(filename,'a')
        self.logger = Logger(f)
        self.tracker_map = UniqueMap()
        self.item_counter = 0
        self.lock = ThreadLock()
    
    def clear(self):
        self.logger.clear_log()
    
    def insert_item(self,item):

        if not issubclass(type(item),ReportItem):
            raise TypeError('item must be of type ReportItem')
        
        if not self.contains_name(item.name):
                with self.lock:
                    self.tracker_map.insert(item.name,True)
                    self.__write(item)

    def get_num_of_items(self):
        return len(self.tracker_map)

    def contains_name(self,name):
        with self.lock:
            b = self.tracker_map.contains(name,True)
    
        return b
    
# private methods
    def __write(self, item):
        self.logger.log(str(item))
    
    


        