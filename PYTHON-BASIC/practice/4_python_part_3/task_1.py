"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
from typing import Union


class WrongFormatException(Exception):
    pass


def calculate_days(from_date: str) -> int:
    try:
        date_obj = datetime.strptime(from_date, "%Y-%m-%d")
    except ValueError:
        raise WrongFormatException("Date format must be YYYY-MM-DD")

    today = datetime.now()
    delta = today.date() - date_obj.date()
    return delta.days
    


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
import pytest
from freezegun import freeze_time
from no_of_days import calculate_days, WrongFormatException


@freeze_time("2021-10-06")
def test_date_in_past():
    assert calculate_days("2021-10-05") == 1


@freeze_time("2021-10-06")
def test_date_in_future():
    assert calculate_days("2021-10-07") == -1


@freeze_time("2021-10-06")
def test_same_day():
    assert calculate_days("2021-10-06") == 0


def test_invalid_format():
    with pytest.raises(WrongFormatException):
        calculate_days("10-07-2021")
