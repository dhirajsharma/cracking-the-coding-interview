import main
import unittest


class MainTest(unittest.TestCase):

    def setUp(self):
        self.expected = 42

    def testSimple(self):
        self.assertEqual(main.simple(), 42)


if __name__ == '__main__':
    unittest.main()
