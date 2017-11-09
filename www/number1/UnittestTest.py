import unittest
class UnittestTest(unittest.TestCase):

    def test_division(self):
        self.assertEquals(self.division(2),5)

    def test_division2(self):
        self.assertEquals(self.division(2),7)

    def test_division3(self):
        self.assertEquals(self.division(0),5)
    def test_division4(self):
        self.assertEquals(self.division(5),2)

    def division(self,key):
        return 10/key
if __name__=="__main__":
    unittest.main()