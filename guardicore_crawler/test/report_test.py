from guardicore_crawler.components.report import Report
import unittest

class TestReport(unittest.TestCase):
    
    def setUp(self):
        self.filename = 'test.txt'
        self.rep = Report(self.filename)
    

    def test_write(self):
        self.rep.clear()
        self.rep.insert_item('http://www.amazon.com')
        self.rep.insert_item('http://www.google.com')
        self.rep.insert_item('http://www.ebay.com')

        self.assertEqual(self.rep.count_items(),3)
        self.assertTrue(self.rep.is_visited('http://www.amazon.com'))
        self.assertTrue(self.rep.is_visited('http://www.google.com'))
        self.assertTrue(self.rep.is_visited('http://www.ebay.com'))

        with open(self.filename,'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines),3)
            self.assertEqual(lines[0],'http://www.amazon.com\n')
            self.assertEqual(lines[1],'http://www.google.com\n')
            self.assertEqual(lines[2],'http://www.ebay.com\n')

        

    def test_no_duplicates(self):
        self.rep.clear()
        self.rep.insert_item('http://www.google.com')
        self.rep.insert_item('http://www.google.com')
        self.rep.insert_item('http://www.google.com')

        self.assertEqual(self.rep.count_items(),1)
        with open(self.filename,'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines),1)
            self.assertEqual(lines[0],'http://www.google.com\n')
            
    # def tearDown(self):
    #     self.rep.clear()
    #     self.rep = None

if __name__ == "__main__":
    unittest.main()