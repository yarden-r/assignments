from threading import Thread
from time import time
class ThreadWrapper:
    def __init__ (self, func, args = ()):
        self.func = func
        self.args = args
        self.thread = None
        self.got = False

    def start (self):
        self.thread = Thread(target = self.func, args = self.args)
        self.thread.start()
        return self.thread


    def join (self, timeout = None):
        start = time()
        self.thred = self.thread.join(timeout = timeout)
        end = time()
        if timeout is not None and end - start > timeout:
            return None
        return self.thread
