from concurrent.futures import ThreadPoolExecutor as Pool
from guardicore_crawler.helpers.singleton import Singleton

class GlobalThreadPool(Singleton):
    def __init__(self):
        self.pool = Pool()
    
    def __enter__(self):
        return self.pool.__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        return self.pool.__exit__(exc_type, exc_value, traceback)
    
    def submit(self, func, *args, **kwargs):
        return self.pool.submit(func, *args, **kwargs)

    def map(self, func, *iterables, **kwargs):
        return self.pool.map(func, *iterables, **kwargs)
    