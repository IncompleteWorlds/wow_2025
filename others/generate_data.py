"""This program retrieves the maximum amount of money an user
has spent"""

import sys
import time
import random

"""Generate a random set of values between 1, N
Each value is between 1 and 10000"""
def generate_data(in_number_items: int, in_save_to_file: bool = False):
    output_buffer = []

    print("Number of values generated: ", in_number_items)
    for i in range(in_number_items):
        a_number = random.randint(1, 100000)
        output_buffer.append(a_number)

    # Save to a file, if requested 
    if in_save_to_file:
        with open("generated_data.csv", "wt") as of:
            for a_number in output_buffer:
                of.write(f"{a_number:d}\n")

    return output_buffer


# =========================================
if len(sys.argv) < 2:
    print("Usage: generate_data   max_number")
    sys.exit(0)

max_number_records = int(sys.argv[1])
new_data_set = generate_data(max_number_records, True)

print("Memory:             ", sys.getsizeof(new_data_set), " bytes")