"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""

# Task 1:

import pytest
from task_parametrize import fibonacci_1, fibonacci_2  

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (10, 55),
    (15, 610),
])
def test_fibonacci_functions(n, expected):
    assert fibonacci_2(n) == expected
    assert fibonacci_1(n) == expected  

# Task 2:


# def fibonacci_1(n):
#     a, b = 0, 1
#     for _ in range(n-1):-------->buggy version
#         a, b = b, a + b
#     return b

def fibonacci_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# def fibonacci_2(n):
#     fibo = [0, 1]
#     for i in range(1, n+1):
#         fibo.append(fibo[i-1] + fibo[i-2])--------> buggy version
#     return fibo[n]

def fibonacci_2(n):
    if n == 0:
        return 0
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n] 
