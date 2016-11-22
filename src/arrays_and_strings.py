CHAPTER = 1


# 1.1
# Is Unique:
# - Implement an alogirthm to determine if a string has all unique characters.
# - What if you cannot use additional data structures?
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
