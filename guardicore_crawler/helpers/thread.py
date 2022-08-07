from threading import Thread

class ThreadWrapper:
    def __init__ (self, func, args = ()):
        self.func = func
        self.args = args
        self.thread = None
    
    def start (self):
        self.thread = Thread(target = self.func, args = self.args)
        self.thread.start()
        return self.thread

    def join (self, timeout = None):
        self.thread.join(timeout = timeout)
        return self.thread
