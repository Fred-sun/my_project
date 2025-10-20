import unittest

class TestAddFunction(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(1 + 2, 3)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)

