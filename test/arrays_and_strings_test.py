import arrays_and_strings as subject
import unittest


class ArraysAndStringsTest(unittest.TestCase):
    def test_chapter(self):
        self.assertEqual(subject.CHAPTER, 1)


class IsUnique(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(subject.is_unique(''), True)

    def test_simple(self):
        self.assertEqual(subject.is_unique('abcdef'), True)

    def test_repeated(self):
        self.assertEqual(subject.is_unique('ababababa'), False)

    def test_worst_case(self):
        self.assertEqual(subject.is_unique('abcdefghijklmnopp'), False)

if __name__ == '__main__':
    unittest.main()
