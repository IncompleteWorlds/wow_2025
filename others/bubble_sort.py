import sys
import random
import time


"""Generate a random set of values between 1, 50000
Each value is between 1 and 10000"""
def generate_data(in_save_to_file: bool = False):
    nb_number = random.randint(1, 50000)
    output_buffer = []

    print("Number of values generated: ", nb_number)
    for i in range(nb_number):
        a_number = random.randint(1, 10000)
        output_buffer.append(a_number)

    # Save to a file, if requested 
    if in_save_to_file:
        with open("test.csv", "wt") as of:
            for a_number in output_buffer:
                of.write(f"{a_number:d}\n")

    return output_buffer

"""Read the complete file and insert each value into 
an array"""
def read_from_file(in_filename: str):
    output_buffer = []
    with open(in_filename, 'r') as number_file:
        for current_line in number_file:
            output_buffer.append(int(current_line.strip()))

    return output_buffer


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    # Swap if they are not ordered
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# =========================================

if len(sys.argv) <= 1:
    print("Usage: bubble_sort   file")
    # sys.exit(0)

    data_buffer = generate_data()

else:
    data_buffer = read_from_file(sys.argv[1])

start_time = time.perf_counter()
result = bubble_sort(data_buffer)
end_time = time.perf_counter()

print("Input array:        ", data_buffer)
print("Memory:             ")
print("Processing time:    ", (end_time - start_time), " secs")
