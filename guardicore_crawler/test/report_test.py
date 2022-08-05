from guardicore_crawler.components.report import Report
from guardicore_crawler.components.report_item import ReportItem
import unittest

class Url(ReportItem):
    def __init__(self,url):
        super().__init__(url)

    def __str__(self):
        return self.url

class TestReport(unittest.TestCase):
    
    def setUp(self):
        self.filename = 'test.txt'
        self.rep = Report(self.filename)
    

    def test_write(self):
        self.rep.clear()
        url1 = Url('http://www.google.com')
        print("the type outside method is ", type(url1))
        self.rep.insert_item(Url('http://www.amazon.com'))
        self.rep.insert_item(url1)
        self.rep.insert_item(Url('http://www.ebay.com'))

        self.assertEqual(self.rep.get_num_of_items(),3)
        self.assertTrue(self.rep.is_visited(Url('http://www.amazon.com')))
        self.assertTrue(self.rep.is_visited(Url('http://www.google.com')))
        self.assertTrue(self.rep.is_visited(Url('http://www.ebay.com')))

        with open(self.filename,'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines),3)
            self.assertEqual(lines[0],'http://www.amazon.com\n')
            self.assertEqual(lines[1],'http://www.google.com\n')
            self.assertEqual(lines[2],'http://www.ebay.com\n')

        print('test_write passed')
        

    def test_no_duplicates(self):
        self.rep.clear()
        self.rep.insert_item(Url('http://www.google.com'))
        self.rep.insert_item(Url('http://www.google.com'))
        self.rep.insert_item(Url('http://www.google.com'))


        self.assertEqual(self.rep.get_num_of_items(),1)
        with open(self.filename,'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines),1)
            self.assertEqual(lines[0],'http://www.google.com\n')

        print('test_no_duplicates passed')

    def tearDown(self):
        self.rep.clear()
        self.rep = None

if __name__ == "__main__":
    unittest.main()