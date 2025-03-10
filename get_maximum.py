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

"""Get the maximum value of the array"""
def get_maximum(in_array):
    maximum_value = 0

    # Process all elements, looking for the maximum
    for i in range(len(in_array)):
        tmp_maximum_value = in_array[i]
        for j in range(len(in_array)):
            if in_array[j] > tmp_maximum_value:
                tmp_maximum_value = in_array[j]

        maximum_value = tmp_maximum_value

    return maximum_value

"""Linear search of an element in an array"""
def linear_search(arr, target):
	for i in range(len(arr)):
			if arr[i] == target:
				return i
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
result = get_maximum(data_buffer)
end_time = time.perf_counter()

print("Maximum value:      ", result)
print("Processing time:    ", (end_time - start_time), " secs")
print("Memory:             ", sys.getsizeof(data_buffer), " bytes")




# Check if our client is the maximum of the month, of all clients
list_values = read_from_file("monthly_user_data.csv")

start_time = time.perf_counter()
index = linear_search(list_values, result)
end_time = time.perf_counter()

print()
print("Processing time:    ", (end_time - start_time), " secs")
print("Memory:             ", sys.getsizeof(list_values), " bytes")

if index != -1:
    print("The user is the winner of the month")
else:
    print("Sorry, you have to keep spending")