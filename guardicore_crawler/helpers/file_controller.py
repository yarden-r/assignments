class FileController(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.file = None
        if mode != 'w' and mode != 'a':
            raise ValueError('Invalid mode: ' + mode)
        self.mode = mode

    def __enter__(self):
        """
        __enter__ is called when the with statement is used.
        This is done here because opening a file can raise an exception.
        """
        self.file = open(self.filename, self.mode)
        if self.file is None:
            print('Error: Could not open file: {}'.format(self.filename))
            raise IOError('Could not open file: ' + self.filename)

        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type is IOError:
            print('Error: {}'.format(exc_value))
            return False
        return True


