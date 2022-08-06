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

    def join (self):
        self.thread.join()
        return self.thread
