"""
List & Dict Comprehension Examples
A quick tour of Pythonic ways to build collections.
"""

# 1. Squares of numbers 1-10
squares = [x ** 2 for x in range(1, 11)]

# 2. Only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]

# 3. Convert list of words to their lengths
words = ["python", "api", "django", "flask", "docker"]
word_lengths = {word: len(word) for word in words}

# 4. Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested for num in sublist]

# 5. Filter and transform in one step: uppercase words longer than 4 chars
long_words_upper = [w.upper() for w in words if len(w) > 4]


if __name__ == "__main__":
    print("Squares:", squares)
    print("Evens:", evens)
    print("Word lengths:", word_lengths)
    print("Flattened:", flattened)
    print("Long words upper:", long_words_upper)
