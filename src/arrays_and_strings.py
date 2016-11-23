CHAPTER = 1

# 1.1 Is Unique: Implement an alogirthm to determine if a string has all unique
# characters. What if you cannot use additional data structures?
def is_unique(string):
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
    ordered = sorted(string)
    for i in range(len(ordered)):
        if i >= len(ordered) - 1:
            continue

        if ordered[i] == ordered[i+1]:
            return False

    return True


# 1.2 Check Permutation: Given two strings, write a method to decide if one is a
# permutation of the other.
def check_permutation(a, b):
    if len(a) != len(b):
        return False

    return sorted(a) == sorted(b)

def check_permutation_alternate(a, b):
    from collections import defaultdict

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

# 1.4 Palindrome Permutation: Given a string, write a function to check if it is
# a permutation of a palindrome.
def palindrome_permutation(phrase):
    from string import ascii_lowercase
    from collections import defaultdict

    counts = defaultdict(lambda: 0)
    odds = 0

    for char in phrase.lower():
        if char in ascii_lowercase:
            counts[char] += 1

    for char in counts:
        if counts[char] % 2 == 1:
            odds += 1
        if odds > 1:
            return False

    return True

# 1.5 One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Given two
# strings, write a function to check if they are one edit (or zero edits) away.
def check_one_replace(a, b):
    assert len(a) == len(b)
    replace = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if replace:
                return False
            else:
                replace = True
    return True

def check_one_insert(a, b):
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1

    return True

def one_or_zero_away(a, b):
    # Assumptions: all characters are letters
    delta = len(a) - len(b)

    if delta == 0:
        return check_one_replace(a, b)
    elif delta == 1:
        return check_one_insert(b, a)
    elif delta == -1:
        return check_one_insert(a, b)
    else:
        return False

# 1.6 String Compression: Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the string "aabccccaaa"
# would become "a2b1c5a3". If the compressed string would not become smaller
# than the original string, your method should return the original string. You
# can assume the string has only uppercase and lowercase letters.
def string_compression(string):
    encoding = []

    previous = None
    count = 0
    for i in range(len(string)):
        char = string[i]
        if char != previous and previous is not None:
            encoding.append(previous + str(count))
            if len(''.join(encoding)) > len(string):
                return string
            count = 0
        count += 1
        previous = char

    if previous is not None:
        encoding.append(previous + str(count))

    encoded = ''.join(encoding)
    if len(string) > len(encoding):
        return encoded
    else:
        return string

# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each
# pixel is in the image is 4 bytes, write a method to rotate the image by 90
# degrees. Can you do this in place?
def rotate_matrix(m):
    try:
        n = len(m)
        assert n == len(m[0])
    except (IndexError, AssertionError):
        return False

    for i in range(n/2):
        a = n - 1 - i
        for j in range(i, a):
            b = j - i
            m[i][j], m[a-b][i], m[a][a-b], m[j][a] = m[a-b][i], m[a][a-b], m[j][a], m[i][j]

    return m

# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix
# is 0, its entire row and column are set to 0.
def zero_matrix(matrix):
    rows = set(range(len(matrix)))
    cols = set(range(len(matrix[0])))

    row_zeros = set([])
    col_zeros = set([])

    for row in rows:
        if row in row_zeros:
            continue

        for col in cols:
            if col in col_zeros:
                continue

            if matrix[row][col] == 0:
                row_zeros.add(row)
                col_zeros.add(col)
                break

    for row in row_zeros:
        for col in cols:
            matrix[row][col] = 0

    for col in col_zeros:
        for row in rows - row_zeros:
            matrix[row][col] = 0

    return matrix


# 1.9 String Rotation: Assume you have a method isSubstring which checks if one
# word is a substring of another. Given two strings, s1 and s2, write code to
# check if s2 is a rotation of s1 using only one call to isSubstring (e.g.
# "waterbottle" is a rotation of "erbottlewat").
def is_substring(s1, s2):
    return s1 in s2

def string_rotation(s1, s2):
    return len(s1) == len(s2) and is_substring(s1, s2*2)
