"""
Task:

Create a function that returns the first n multiples of x.

Example:

count_by(3, 5) -> [3, 6, 9, 12,15]
"""

def count_by(x, n):
    new_list = []

    for i in range(1, n + 1):
        new_list.append(x * i)

    return new_list


