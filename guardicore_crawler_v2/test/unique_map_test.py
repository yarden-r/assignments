import unittest
from guardicore_crawler_v2.helpers.unique_map import UniqueMap

class UniqueMapTest(unittest.TestCase):
    def setUp(self):
        self.um = UniqueMap()
    
    def test_insert(self):
        self.um.insert('a',1)
        self.um.insert('b',2)
        self.um.insert('c',3)
        self.um.insert('d',4)
        self.um.insert('e',5)
        self.um.insert('f',6)
        self.um.insert('g',7)
        self.um.insert('h',8)
        self.um.insert('i',9)
        self.um.insert('j',10)
        self.um.insert('k',11)
        self.um.insert('l',12)
        self.um.insert('m',13)
        self.um.insert('n',14)
        self.um.insert('o',15)
        self.um.insert('p',16)
        self.um.insert('q',17)
        self.um.insert('r',18)
        self.um.insert('s',19)
        self.um.insert('t',20)
        self.um.insert('u',21)
        self.um.insert('v',22)
        self.um.insert('w',23)
        self.um.insert('x',24)
        self.um.insert('y',25)
        self.um.insert('z',26)
        self.assertEqual(26,len(self.um))

    def test_no_duplicates(self):
        self.um.insert('a',40)
        self.um.insert('a',41)
        self.assertEqual(1,len(self.um))


if __name__ == '__main__':
    unittest.main()
    