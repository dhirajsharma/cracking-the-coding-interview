import arrays_and_strings as subject
import unittest


class ArraysAndStringsTest(unittest.TestCase):

    def setUp(self):
        pass

    def testChapter(self):
        self.assertEqual(subject.CHAPTER, 1)

if __name__ == '__main__':
    unittest.main()
