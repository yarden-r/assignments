from guardicore_crawler_v2.helpers.singleton import Singleton

class GlobalQueue(Singleton):
    def __init__(self):
        self.queue = []
    
    def append(self,item):
        self.queue.append(item)
    
    def pop(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)
    
    #make iteratable
    def __iter__(self):
        return self.queue.__iter__()
        