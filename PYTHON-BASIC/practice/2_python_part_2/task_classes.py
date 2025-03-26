"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""

import datetime
from typing import Optional


class Homework:
    
    def __init__(self, text: str, days: int):
        self.text = text
        self.created = datetime.datetime.now()  # Capture the exact time when the homework is created
        self.deadline = datetime.timedelta(days=days)  # Set the deadline using timedelta

    def is_active(self) -> bool:
        """Check if the homework deadline is still valid."""
        return datetime.datetime.now() < self.created + self.deadline  


class Student:
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: Homework) -> Optional[Homework]:
        if homework.is_active():
            return homework  # Homework is still valid, so the student can do it
        print("You are late")  # Homework is expired
        return None


class Teacher:
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        """Creates and returns a Homework object."""
        return Homework(text, days)


# Test cases
if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2024-03-21 09:30:00.123456
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # Creating another homework
    create_homework_too = teacher.create_homework  # Assign method to a variable
    oop_homework = create_homework_too('Create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    # Student attempts homework
    student.do_homework(oop_homework)  # Allowed
    student.do_homework(expired_homework)  # "You are late"
