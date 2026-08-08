"""
Palindrome Checker
Checks whether a given string is a palindrome,
ignoring spaces, punctuation, and case.
"""

import re


def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_cases = [
        "Madam",
        "A man a plan a canal Panama",
        "Hello World",
        "Was it a car or a cat I saw?",
    ]

    for case in test_cases:
        result = is_palindrome(case)
        print(f"'{case}' -> {'Palindrome' if result else 'Not a palindrome'}")
