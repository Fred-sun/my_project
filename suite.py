import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

class TestAddMoreFunction(unittest.TestCase):
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

# 创建测试套件
suite = unittest.TestSuite()
suite.addTest(TestAddFunction('test_add_positive'))
suite.addTest(TestAddFunction('test_add_negative'))
suite.addTest(TestAddMoreFunction('test_add_zero'))

# 运行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)

