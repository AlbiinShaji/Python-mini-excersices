"""
File Read/Write Example
Writes some sample data to a CSV file, then reads it back
and prints it out.
"""

import csv
import os

FILENAME = "sample_data.csv"


def write_csv():
    data = [
        ["name", "role", "language"],
        ["Alby", "Intern", "Python"],
        ["Priya", "Developer", "Django"],
        ["Rahul", "DevOps", "Docker"],
    ]

    with open(FILENAME, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print(f"Wrote data to {FILENAME}")


def read_csv():
    with open(FILENAME, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    write_csv()
    print("\nReading back the file:\n")
    read_csv()

    # Clean up the generated file after demo
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
