"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

# task_4.py
import argparse
from faker import Faker
import sys
import json


def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()
    for _ in range(args.number):
        result = {}
        for field, provider in args.fields.items():
            try:
                result[field] = getattr(fake, provider)()
            except AttributeError:
                print(f"Provider '{provider}' is not valid.", file=sys.stderr)
                return
        print(json.dumps(result))


def main():
    parser = argparse.ArgumentParser(description="Generate fake data using Faker")
    parser.add_argument("number", type=int, help="Number of fake data instances to generate")
    
    # Parse known and unknown args
    known_args, unknown_args = parser.parse_known_args()
    
    # Convert --field=provider to a dictionary
    fields = {}
    for item in unknown_args:
        if item.startswith("--") and "=" in item:
            key, value = item[2:].split("=", 1)
            fields[key] = value

    known_args.fields = fields
    print_name_address(known_args)


if __name__ == "__main__":
    main()

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
# test_task_4.py
from unittest.mock import Mock
from task4 import print_name_address


def test_print_name_address(capfd):
    mock_args = Mock()
    mock_args.number = 1
    mock_args.fields = {
        "username": "name",
        "emailAddress": "email"
    }

    print_name_address(mock_args)
    
    out, err = capfd.readouterr()


    assert "username" in out
    assert "emailAddress" in out


