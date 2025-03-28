"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

def create_sample_files(directory: str): # Creates sample text files with predefined values.
    os.makedirs(directory, exist_ok=True)  # Create directory if not exists

    file_data = {
        "file_1.txt": "23",
        "file_2.txt": "78",
        "file_3.txt": "3"
    }

    for filename, content in file_data.items():
        with open(os.path.join(directory, filename), "w") as file:
            file.write(content)

def extract_and_write_values(directory: str, output_file: str): # Reads values from files in directory and writes them to output file.
    values = []

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in sorted(os.listdir(directory)):  
        file_path = os.path.join(directory, filename)

        with open(file_path, "r") as file:
            value = file.read().strip()  # Read and remove whitespace
            values.append(value)

    with open(output_file, "w") as output:
        output.write(", ".join(values))

    print(f"Values successfully written to {output_file}")

    # Print the result.txt content to check the output
    with open(output_file, "r") as output:
        print("Final Output:", output.read())


create_sample_files("./files")


extract_and_write_values("./files", "result.txt")  # Then extract and write values
