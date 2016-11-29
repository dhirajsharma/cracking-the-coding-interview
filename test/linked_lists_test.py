import linked_lists as subject
import unittest

class LinkedListsTest(unittest.TestCase):
    def test_chapter(self):
        self.assertEqual(subject.CHAPTER, 2)

    def test_linked_list(self):
        ll = subject.LinkedList()
        ll.append('alpha')
        ll.append('bravo')
        ll.append('charlie')
        self.assertEqual([node.value for node in ll.list()], ['alpha', 'bravo', 'charlie'])

if __name__ == '__main__':
    unittest.main()
