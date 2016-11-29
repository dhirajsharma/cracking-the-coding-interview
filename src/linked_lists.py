CHAPTER = 2

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class First:
    pass

class LinkedList:
    def __init__(self, *values):
        self.first = None
        self.last = None

        for value in values:
            self.append(value)

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def append(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def list(self, start=First):
        if start == First:
            start = self.first

        if start is None:
            return []
        else:
            return [start] + self.list(start.next)

    def values(self):
        return [node.value for node in self.list()]

    def clear(self):
        self.__init__()

# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?
def remove_duplicates(linked_list):
    return linked_list

# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element
# of a singly linked list.
def last(linked_list, k):
    return linked_list.last

# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e. any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.
def delete_node(linked_list, node):
    return linked_list

# 2.4 Partition: Write code to partition a linked list around a value x, such
# that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be after the
# elements less than x. The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right
# partitions.
def partition(linked_list, x):
    return linked_list

# 2.5 Sum Lists: You have two numbers represented by a linked list, where each
# node contains a single digit. The digits are stored in reverse order such that
# the 1's digit is at the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.
def sum_lists(l1, l2):
    return l1 + l2

# 2.6 Palindrome: Create a function to check if a linked list is a palindrome.
def is_palindrome(linked_list):
    return False

# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists
# intersect. Return the intersecting node. Note that the intersection is defined
# based on reference, not value. That is, if the kth node of the first linked
# list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.
def intersection(l1, l2):
    pass

# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that
# returns the node at the beginning of the loop.
def detect_loop(linked_list):
    pass
