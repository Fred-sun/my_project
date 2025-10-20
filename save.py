import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(1 + 2, 3)

if __name__ == "__main__":
    # 打开文件并将输出重定向到文件
    with open('result.txt', 'w') as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
