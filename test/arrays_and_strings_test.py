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

class OneOrZeroAwayTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subject.one_or_zero_away('', ''), True)

    def test_trivial(self):
        self.assertEqual(subject.one_or_zero_away('abc', 'abcde'), False)

    def test_same(self):
        self.assertEqual(subject.one_or_zero_away('abc', 'abc'), True)

    def test_remove(self):
        self.assertEqual(subject.one_or_zero_away('pale', 'ple'), True)

    def test_insert(self):
        self.assertEqual(subject.one_or_zero_away('pale', 'pales'), True)

    def test_replace(self):
        self.assertEqual(subject.one_or_zero_away('pale', 'pile'), True)

    def test_two_edits(self):
        self.assertEqual(subject.one_or_zero_away('pale', 'bake'), False)

    def test_three_edits(self):
        self.assertEqual(subject.one_or_zero_away('pale', 'bike'), False)

    def test_reordered_edits(self):
        self.assertEqual(subject.one_or_zero_away('pale', 'elap'), False)

class StringCompressionTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subject.string_compression(''), '')

    def test_would_be_smaller(self):
        self.assertEqual(subject.string_compression('aabcccccaaa'), 'a2b1c5a3')

    def test_would_be_larger(self):
        self.assertEqual(subject.string_compression('abcdefg'), 'abcdefg')

    def test_mixed_case(self):
        self.assertEqual(subject.string_compression('aaaAAAaaa'), 'a3A3a3')

if __name__ == '__main__':
    unittest.main()
