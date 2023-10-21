"""
Problem
1. Implement an algorithm to determine if a string has all unique characters. 
2. What if you cannot use additional data structures

Questions I have:
1. Can the string come in empty?
2. Is there a cap on how big the string can be?
3. Are we counting a lowercase letter and an upper case letter as a repeated character?
"""


def set_approach(s: str) -> bool:
    """
    This approach uses a set to determine if the string is unique or not. This

    Time Complexity:
        0(N) where N is size of the string
    Space Compexity:
        O(1)
    """

    # set to see keep track of variables in the list
    setty = set()

    # adding char if not in set and returning False if seen before
    for i in s:
        if i not in setty:
            setty.add(i)
        elif i in setty:
            return False

    # returning true if it is never in the set
    return True


def no_other_data_structure(s: str) -> bool:
    """
    this just sorts the string to put any duplicate occurences next to each other

    Time Complexity:
        0(n log(n)) due to sorting the string
    Space Compexity:
        O(1)
    """

    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True


if __name__ == "__main__":
    print(set_approach("helo"))
    print(no_other_data_structure("abcdefghijklmnopaqrstuvwxyz"))
