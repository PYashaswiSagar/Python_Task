import os
from random import randint
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import csv

# Directory where we store outputs
OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


# === FIBONACCI FUNCTION ===
def fib(n: int):
    """Calculate the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    f0, f1 = 0, 1
    for _ in range(2, n + 1):
        f0, f1 = f1, f0 + f1
    return f1


# === FUNC1: Calculate and Save to Files ===
def write_fib_to_file(n: int):
    """Calculate Fibonacci number and write to a file."""
    result = fib(n)
    file_path = os.path.join(OUTPUT_DIR, f"{n}.txt")
    with open(file_path, 'w') as f:
        f.write(str(result))
    return file_path  # optional, useful for debugging


def func1(array: list):
    """Calculate Fibonacci numbers in parallel and write them to individual files."""
    # Use multiple processes for CPU-bound computation
    with ProcessPoolExecutor() as executor:
        executor.map(write_fib_to_file, array)


# === FUNC2: Read Files and Combine ===
def read_fib_from_file(file_path: str):
    """Read the number from a file and return (ordinal, value) pair."""
    filename = os.path.basename(file_path)
    ordinal = int(filename.split('.')[0])
    with open(file_path, 'r') as f:
        value = f.read().strip()
    return ordinal, value


def func2(result_file: str):
    """Read all .txt files and combine them into one CSV."""
    files = [os.path.join(OUTPUT_DIR, f) for f in os.listdir(OUTPUT_DIR) if f.endswith('.txt')]

    results = []

    # Use threads for fast I/O-bound operations
    with ThreadPoolExecutor() as executor:
        for result in executor.map(read_fib_from_file, files):
            results.append(result)

    # Sort results by ordinal (optional)
    results.sort()

    # Write to CSV
    with open(result_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for ordinal, value in results:
            writer.writerow([ordinal, value])


# === MAIN SCRIPT ===
if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Generate a list of 1000 random Fibonacci indexes (can be very large)
    numbers = [randint(1000, 100000) for _ in range(1000)]

    # Step 1: Calculate and save each Fibonacci number in a separate file
    func1(numbers)

    # Step 2: Read all files and write them to one CSV file
    func2(result_file=RESULT_FILE)

