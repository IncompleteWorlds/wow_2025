"""This program retrieves the maximum amount of money an user
has spent"""

import sys
import time
import random

"""Generate a random set of values between 1, 100000
Each value is between 1 and 10000"""
def generate_data(in_save_to_file: bool = False):
    nb_number = random.randint(1, 100000)
    output_buffer = []

    print("Number of values generated: ", nb_number)
    for i in range(nb_number):
        a_number = random.randint(1, 100000)
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


def insertion_sort(arr):
    for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    return arr

"""Get the maximum value of the array"""
def get_maximum_sorted_insert(in_array):
    new_array = insertion_sort(in_array)

    return new_array[-1]


"""Linear search of an element in an array"""
def linear_search(arr, target):
	for i in range(len(arr)):
			if arr[i] == target:
				return i
	return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# =========================================

if len(sys.argv) < 2:
    print("Usage: get_maximum   filename")
    # sys.exit(0)

    data_buffer = generate_data()

else:
    data_buffer = read_from_file(sys.argv[1])

# Give 5% discount to our best client. Whoever spends more money
# Look for the maximum expenditure of our client 


start_time = time.perf_counter()
result = get_maximum_sorted_insert(data_buffer)
end_time = time.perf_counter()

print("Maximum value:      ", result)
print("Processing time:    ", (end_time - start_time), " secs")
print("Memory:             ", sys.getsizeof(data_buffer), " bytes")




# Check if our client is the maximum of the month
list_values = read_from_file("monthly_user_data.csv")

start_time = time.perf_counter()
# index = linear_search(list_values, result)
index = binary_search(list_values, result)
end_time = time.perf_counter()

print()
print("Processing time:    ", (end_time - start_time), " secs")
print("Memory:             ", sys.getsizeof(list_values), " bytes")

if index != -1:
    print("The user is the winner of the month")
else:
    print("Sorry, you have to keep spending")