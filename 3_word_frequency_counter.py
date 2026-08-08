"""
Word Frequency Counter
Reads a block of text and counts how often each word appears.
"""

from collections import Counter
import re


def word_frequency(text: str) -> dict:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return dict(Counter(words))


if __name__ == "__main__":
    sample_text = """
    Python is great. Python is easy to learn.
    Learning Python opens many doors in software development.
    """

    freq = word_frequency(sample_text)

    # Print sorted by frequency, highest first
    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")
