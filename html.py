import unittest
import HtmlTestRunner

class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(1 + 2, 3)

if __name__ == "__main__":
    # 打开 HTML 文件
    with open("result.html", "w") as f:
        runner = HtmlTestRunner.HTMLTestRunner(output='test.log', verbosity=2, stream=f)
        #runner = HtmlTestRunner.HTMLTestRunner(stream=f, verbosity=2, description="Test Results")
        #runner = HtmlTestRunner.HTMLTestRunner(stream=f, verbosity=2, title="Test Report", description="Test Results")
        unittest.main(testRunner=runner)
