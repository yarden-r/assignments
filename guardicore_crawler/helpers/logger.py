from guardicore_crawler.helpers.file_controller import FileController

"""
    Logs a message to a file.
"""
class Logger(object):
   
#public methods
    def __init__(self,file:FileController):
        self.file = file

    def log(self,message):
        with self.file as f:
            f.write(message + '\n')
            f.close()
    
    def clear_log(self):
        with self.file as f:
            f.seek(0)
            f.truncate()
            f.close()
    