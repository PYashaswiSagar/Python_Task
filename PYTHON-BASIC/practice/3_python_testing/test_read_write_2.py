"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import os
# import string
# import random
import pytest
from pathlib import Path

from task_read_write_2 import write_words_to_files

def test_write_words_to_files(tmp_path):
    # Step 1: Prepare test data
    test_words = ["apple", "banana", "cherry"]

    # Step 2: Change current working directory to tmp_path (safe test environment)
    original_cwd = Path.cwd()
    try:
        # Switch to the temporary path for file creation
        os.chdir(tmp_path)

        # Step 3: Call the function to write files
        write_words_to_files(test_words)

        # Step 4: Define expected file paths
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"

        # Step 5: Check if files exist
        assert file1.exists(), "file1.txt was not created"
        assert file2.exists(), "file2.txt was not created"

        # Step 6: Check contents of file1 (UTF-8, newline separated)
        with open(file1, "r", encoding="utf-8") as f:
            content1 = f.read().strip()
        expected1 = "\n".join(test_words)
        assert content1 == expected1, f"file1.txt content mismatch. Expected: {expected1}, Got: {content1}"

        # Step 7: Check contents of file2 (CP1252, reverse order, comma separated)
        with open(file2, "r", encoding="cp1252") as f:
            content2 = f.read().strip()
        expected2 = ",".join(reversed(test_words))
        assert content2 == expected2, f"file2.txt content mismatch. Expected: {expected2}, Got: {content2}"

    finally:
        # Step 8: Restore original working directory
        os.chdir(original_cwd)
