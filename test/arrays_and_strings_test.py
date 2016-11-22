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

class URLifyTest(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(subject.urlify('abcdefgh'), 'abcdefgh')

    def test_one_space(self):
        self.assertEqual(subject.urlify('abc cba  '), 'abc%20cba')

    def test_multiple_spaces(self):
        self.assertEqual(subject.urlify('abc  cba bca      '), 'abc%20%20cba%20bca')

class PalindromePermutationTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subject.palindrome_permutation(''), True)

    def test_example(self):
        self.assertEqual(subject.palindrome_permutation("Tact Coa"), True)

    def test_not_palindrome(self):
        self.assertEqual(subject.palindrome_permutation("A, Race. Car!"), False)

    def test_really_long_string(self):
        self.assertEqual(subject.palindrome_permutation('a' * 10**6 + 'b'), True)

if __name__ == '__main__':
    unittest.main()
