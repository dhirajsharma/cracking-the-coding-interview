CHAPTER = 1

# 1.1 Is Unique: Implement an alogirthm to determine if a string has all unique
# characters. What if you cannot use additional data structures?
def is_unique(string):
    # O(1) trivial case
    if len(string) > 128:
        return False

    # O(n) implementation
    return is_unique_with_hash(string)

    # O(n^2) time, O(1) space
    # return is_unique_without_hash(string)

def is_unique_with_hash(string):
    seen = {}
    for char in string:
        if char in seen:
            return False
        else:
            seen[char] = True
    return True

def is_unique_without_hash(string):
    # O(n*log(n)) time (sorted)
    ordered = sorted(string)        # O(log(n))
    for i in range(len(ordered)):   # O(n)
        if i >= len(ordered) - 1:
            continue

        if ordered[i] == ordered[i+1]:
            return False

    return True


# 1.2 Check Permutation: Given two strings, write a method to decide if one is a
# permutation of the other.
def check_permutation(a, b):
    # O(1) time trivial solution
    if len(a) != len(b):
        return False

    # O(2*log(n))
    return sorted(a) == sorted(b)

def check_permutation_alternate(a, b):
    from collections import defaultdict

    # O(1) time trivial solution
    if len(a) != len(b):
        return False

    counts = defaultdict(lambda: 0)
    for char in a:
        counts[char] += 1
    for char in b:
        counts[char] -= 1
        if counts[char] < 0:
            return False

    return sum(counts.values()) == 0

# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You
# may assume that the string has sufficient space at the end to hold the
# additional characters, and that you are given the "true" length of the string.
def urlify(string):
    # return string.replace(' ', '%20')
    return ''.join([c if c != ' ' else '%20' for c in string.strip()])
