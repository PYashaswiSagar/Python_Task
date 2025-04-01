"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""

import string
import random

def generate_words(n=20):
    """Generate random words."""
    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)
    return words

def write_words_to_files(words):
    """Write generated words to two files with different encodings and formats."""
    # Write to file1.txt (UTF-8 encoding, newline separator)
    with open("file1.txt", "w", encoding="utf-8") as file1:
        file1.write("\n".join(words))  # Join words with '\n'

    # Write to file2.txt (CP1252 encoding, reverse order, comma separator)
    with open("file2.txt", "w", encoding="cp1252") as file2:
        file2.write(",".join(reversed(words)))  # Reverse words and join with ','

    print("Words written successfully to file1.txt (UTF-8) and file2.txt (CP1252).")

    # Print the contents of file1.txt (UTF-8)
    print("Content of file1.txt (UTF-8):")
    with open("file1.txt", "r", encoding="utf-8") as file1:
        print(file1.read())  # Print content of file1.txt

    # Print the contents of file2.txt (CP1252)
    print("\nContent of file2.txt (CP1252):")
    with open("file2.txt", "r", encoding="cp1252") as file2:
        print(file2.read())  # Print content of file2.txt

# Generate 3 sample words (you can change the number for more words)
words = generate_words(3)  # Example with 3 words

# Call function to write and print the content
write_words_to_files(words)
