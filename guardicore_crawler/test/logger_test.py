from guardicore_crawler.helpers.logger import Logger

from guardicore_crawler.helpers.file_controller import FileController

import unittest

class TestLogger(unittest.TestCase):

    #setup and teardown
    def setUp(self):
        self.filename = 'test.txt'
        mode = 'w'
        file = FileController(self.filename, mode)
        self.logger = Logger(file)

    def test_log(self):
        self.logger.log('Hello World')
        with open(self.filename, 'r') as f:
            self.assertEqual(f.read(), 'Hello World\n')

    def test_log_append(self):
        filename = 'test.txt'
        mode = 'a'
        file = FileController(filename, mode)
        self.logger = Logger(file)
        self.logger.clear_log()
        self.logger.log('Hello World')
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), 'Hello World\n')
        self.logger.log('Hello World')
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), 'Hello World\nHello World\n')
            
    def test_different_types(self):
        pass
        
if __name__ == '__main__':
    unittest.main()