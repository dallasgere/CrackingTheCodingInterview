def check_permutation(s: str, t: str) -> bool:
    """
    Assuming if they are of different length then we return false

    Time Complexity:
        O(n log n) because of sorting

    Space Complexity:
        O(n)
    """

    if len(s) != len(t):
        return False

    s = sorted(s.lower())
    t = sorted(t.lower())

    return s == t


print(check_permutation("hello", "ollhe"))
print(check_permutation("dallas", "taylor"))
