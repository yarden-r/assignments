from file_controller import FileController

class Logger(object):
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
    