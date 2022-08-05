from guardicore_crawler.helpers.logger import Logger

from guardicore_crawler.helpers.file_controller import FileController

import unittest

class TestLogger(unittest.TestCase):
    def test_log(self):
        filename = 'test.txt'
        mode = 'w'
        file = FileController(filename, mode)
        logger = Logger(file)
        logger.log('Hello World')
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), 'Hello World\n')

    def test_log_append(self):
        filename = 'test.txt'
        mode = 'a'
        file = FileController(filename, mode)
        logger = Logger(file)
        logger.clear_log()
        logger.log('Hello World')
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), 'Hello World\n')
        logger.log('Hello World')
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), 'Hello World\nHello World\n')
if __name__ == '__main__':
    unittest.main()