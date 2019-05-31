import unittest


class IntegerArithmeticTestCase(unittest.TestCase):
    '''测试用例类的注释'''

    @classmethod
    def setUpClass(cls):
        print("first=============first")

    @classmethod
    def tearDownClass(cls):
        print("last===============last")

    def setUp(self):
        print("11111111111111111111111")

    def tearDown(self):
        print("2222222222222222222222222")

    def testAdd(self):  # test method names begin with 'test'
        '''testAdd的注释'''
        print("add==============add")
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        '''testMultiply的注释'''
        print("multiply============multiply")
        self.assertEqual((0 * 10), 1)
        self.assertEqual((5 * 8), 40)

    def testEqual(self):
        '''testEqual的注释'''
        a = "admin"
        b = 'admin1'
        # self.assertEqual(a, b)
        self.assertNotEqual(a, b)


if __name__ == '__main__':

    print(__name__)
    print(unittest.__name__)
    unittest.main()
