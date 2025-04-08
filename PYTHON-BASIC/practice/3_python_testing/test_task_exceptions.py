"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""


import pytest
from task_exceptions import division, DivisionByOneException

#Test when y == 0 (should return None and print message)
def test_division_by_zero(capfd):
    result = division(1, 0)
    out, _ = capfd.readouterr()
    
    assert result is None, "Expected None when dividing by zero"
    assert "Division by 0" in out, "'Division by 0' not printed"
    assert "Division finished" in out, "'Division finished' not printed"


#Test when y == 1 (should raise custom exception)
def test_division_by_one(capfd):
    with pytest.raises(DivisionByOneException):
        division(1, 1)
    
    out, _ = capfd.readouterr()
    assert "Division finished" in out, "'Division finished' not printed"


# Test when division is successful
def test_division_normal(capfd):
    result = division(6, 3)
    out, _ = capfd.readouterr()

    assert result == 2, "Expected 6 // 3 to equal 2"
    assert "Division finished" in out, "'Division finished' not printed"
