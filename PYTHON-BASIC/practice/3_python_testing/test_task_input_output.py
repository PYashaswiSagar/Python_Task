"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
import pytest
# import unittest

from unittest.mock import patch
from task_input_output import read_numbers  # Adjust this to your file/module name


def test_read_numbers_without_text_input():
    # Simulate user inputs: all valid numbers
    user_inputs = ['1', '2', '3', '4']

    with patch('builtins.input', side_effect=user_inputs):
        result = read_numbers(len(user_inputs))
    
    assert result == "Avg: 2.5", f"Expected 'Avg: 2.5', but got '{result}'"


def test_read_numbers_with_text_input():
    # Simulate user inputs: mix of numbers and invalid text
    user_inputs = ['1', '2', 'hello', '3', 'world']

    with patch('builtins.input', side_effect=user_inputs):
        result = read_numbers(len(user_inputs))
    
    assert result == "Avg: 2.0", f"Expected 'Avg: 2.0', but got '{result}'"


def test_read_numbers_all_invalid_input():
    # Simulate user inputs: all invalid
    user_inputs = ['foo', 'bar', 'baz', '123abc', 'hi']

    with patch('builtins.input', side_effect=user_inputs):
        result = read_numbers(len(user_inputs))

    assert result == "No numbers entered", f"Expected 'No numbers entered', but got '{result}'"

