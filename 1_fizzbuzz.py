"""
FizzBuzz
Print numbers 1 to 100.
For multiples of 3 -> "Fizz"
For multiples of 5 -> "Buzz"
For multiples of both 3 and 5 -> "FizzBuzz"
"""

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(100)
