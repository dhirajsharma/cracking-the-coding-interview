import linked_lists as subject
import unittest

class LinkedListsTest(unittest.TestCase):
    def test_chapter(self):
        self.assertEqual(subject.CHAPTER, 2)

    def test_linked_list(self):
        ll = subject.LinkedList('alpha', 'bravo', 'charlie')
        self.assertEqual(ll.values(), ['alpha', 'bravo', 'charlie'])

class RemoveDuplicatesTest(unittest.TestCase):
    def test_unique(self):
        ll = subject.LinkedList('alpha', 'bravo', 'charlie')
        self.assertEqual(subject.remove_duplicates(ll).list(), ll.list())

    def test_duplicates(self):
        ll = subject.LinkedList('alpha', 'alpha', 'bravo')
        self.assertEqual(subject.remove_duplicates(ll).values(), ['alpha', 'bravo'])

class ReturnKthToLastTest(unittest.TestCase):
    pass

class DeleteMiddleNodeTest(unittest.TestCase):
    pass

class PartitionTest(unittest.TestCase):
    pass

class SumListsTest(unittest.TestCase):
    pass

class PalindromeTest(unittest.TestCase):
    pass

class IntersectionTest(unittest.TestCase):
    pass

class LoopDetectionTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
