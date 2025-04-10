"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math

class OperationNotFoundException(Exception):
    pass

def math_calculate(function: str, *args):
    if not hasattr(math, function):
        raise OperationNotFoundException(f"No such function '{function}' in math module")
    
    func = getattr(math, function)

    try:
        return func(*args)
    except TypeError as e:
        raise TypeError(f"{function} requires a different number of arguments: {e}")


"""
Write tests for math_calculate function
"""
import pytest
from math_calculate import math_calculate, OperationNotFoundException

def test_log_with_two_arguments():
    assert math_calculate('log', 1024, 2) == 10.0

def test_ceil_with_one_argument():
    assert math_calculate('ceil', 10.7) == 11

def test_operation_not_found():
    with pytest.raises(OperationNotFoundException):
        math_calculate('unknown_func', 1)

def test_wrong_number_of_arguments_too_many():
    with pytest.raises(TypeError):
        math_calculate('sqrt', 4, 5)

def test_wrong_number_of_arguments_too_few():
    with pytest.raises(TypeError):
        math_calculate('pow')  # needs 2 args



