import arrays_and_strings as subject
import unittest

class ArraysAndStringsTest(unittest.TestCase):
    def test_chapter(self):
        self.assertEqual(subject.CHAPTER, 1)

class IsUniqueTest(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(subject.is_unique(''), True)

    def test_simple(self):
        self.assertEqual(subject.is_unique('abcdef'), True)

    def test_repeated(self):
        self.assertEqual(subject.is_unique('ababababa'), False)

    def test_worst_case(self):
        self.assertEqual(subject.is_unique('abcdefghijklmnopp'), False)

class CheckPermutationTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subject.check_permutation('', ''), True)

    def test_same(self):
        self.assertEqual(subject.check_permutation('abc', 'abc'), True)

    def test_simple(self):
        self.assertEqual(subject.check_permutation('abc', 'cba'), True)

    def test_uneven_lengths(self):
        self.assertEqual(subject.check_permutation('awejfoiawjef', 'ajkwlf'), False)

if __name__ == '__main__':
    unittest.main()
