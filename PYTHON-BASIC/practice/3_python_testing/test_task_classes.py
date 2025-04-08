"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import datetime
import pytest
from task_classes import Homework, Student, Teacher


def test_homework_is_active_true():
    homework = Homework("Do math", 2)
    assert homework.is_active() is True


def test_homework_is_active_false():
    homework = Homework("Do math", 0)
    # Simulate expired by shifting creation time into the past
    homework.created -= datetime.timedelta(days=1)
    assert homework.is_active() is False


def test_homework_negative_days():
    with pytest.raises(ValueError):
        # We'll change Homework later to raise ValueError if days < 0
        Homework("Impossible homework", -3)


def test_teacher_creates_homework():
    teacher = Teacher("John", "Doe")
    hw = teacher.create_homework("Test OOP", 3)
    assert isinstance(hw, Homework)
    assert hw.text == "Test OOP"
    assert hw.deadline == datetime.timedelta(days=3)


def test_student_can_do_active_homework():
    student = Student("Alice", "Smith")
    hw = Homework("Read book", 5)
    result = student.do_homework(hw)
    assert result == hw


def test_student_cannot_do_expired_homework(capfd):
    student = Student("Alice", "Smith")
    hw = Homework("Old task", 0)
    hw.created -= datetime.timedelta(days=1)  # Force expired

    result = student.do_homework(hw)
    assert result is None

    # Also test if "You are late" message was printed
    captured = capfd.readouterr()
    assert "You are late" in captured.out
