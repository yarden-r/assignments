from threading import Lock
class ThreadLock(object):
    def __init__ (self):
        self.my_lock = Lock()
    # def lock (self):
    #     with self.lock:
    #         return self.lock.acquire()
    # def unlock (self):
    #     with self.lock:
    #         return self.lock.release()

    def __enter__ (self):
        self.my_lock.acquire()
        return self




    def __exit__ (self, exc_type, exc_value, traceback):
        self.my_lock.release()
        return False
    