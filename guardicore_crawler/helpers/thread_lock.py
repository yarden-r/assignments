from threading import Lock
class ThreadLock:
    def __init__ (self):
        self.my_lock = Lock()
    # def lock (self):
    #     with self.lock:
    #         return self.lock.acquire()
    # def unlock (self):
    #     with self.lock:
    #         return self.lock.release()
    def lock (self):
        self.my_lock.acquire()
    
    def unlock (self):
        self.my_lock.release()

    def __enter__ (self):
        self.lock()
    def __exit__ (self, type, value, traceback):
        self.unlock()
        return False
    