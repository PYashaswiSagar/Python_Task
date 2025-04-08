"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
# test_task_read_write.py

import os
from read_write import extract_and_write_values

def test_extract_and_write_values(tmp_path):
    # Create temp input files inside a temp directory
    input_dir = tmp_path / "files"
    input_dir.mkdir()

    # Write the sample content to these files
    file_contents = {
        "file_1.txt": "23",
        "file_2.txt": "78",
        "file_3.txt": "3"
    }

    for filename, content in file_contents.items():
        file_path = input_dir / filename
        file_path.write_text(content)

    # Define the output file path (inside tmp folder)
    output_file = tmp_path / "result.txt"

    # Call the function we're testing
    extract_and_write_values(str(input_dir), str(output_file))

    # Read the content of the output file
    result = output_file.read_text()

    # Assert that the result is as expected
    assert result == "23, 78, 3"
