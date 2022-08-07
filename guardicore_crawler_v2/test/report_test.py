from guardicore_crawler.components.report import Report
from guardicore_crawler.components.report_item import ReportItem
import unittest

class Url(ReportItem):
    def __init__(self,url):
        super().__init__(url)

    def __str__(self):
        return self.name

class Animal(ReportItem):
    def __init__(self,name, description):
        super().__init__(name)
        self.description = description

    def __str__(self):
        return self.name + ': ' + self.description

class BrokenUrl(ReportItem):
    def __init__(self,url):
        super().__init__(url)

    def __str__(self):
        return self.name + ' - Broken'
class TestReport(unittest.TestCase):
    
    def setUp(self):
        self.filename = 'test.txt'
        self.rep = Report(self.filename)
    

    def test_write(self):
        self.rep.clear()
        url1 = Url('http://www.amazon.com')
        url2 = Url('http://www.google.com')
        url3 = Url('http://www.ebay.com')

        self.rep.insert_item(url1)
        self.rep.insert_item(url2)
        self.rep.insert_item(url3)

        self.assertEqual(self.rep.get_num_of_items(),3)

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
    # unittest.main()

    animal1 = Animal('cat', 'cute and furry')
    animal2 = Animal('dog', 'happy and hungry')
    animal3 = Animal('rhino', 'angry and loud')
    animal4 = animal1

    rep = Report('test.txt')
    rep.clear()
    rep.insert_item(animal1)
    rep.insert_item(animal2)
    rep.insert_item(animal3)
    rep.insert_item(animal4)

    broken1 = BrokenUrl('http://www.google.com')
    broken2 = BrokenUrl('http://www.google.com')

    rep.insert_item(broken1)
    rep.insert_item(broken2)
