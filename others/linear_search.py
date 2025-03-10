import time
import sys

def linear_search(arr, target):
	for i in range(len(arr)):
			if arr[i] == target:
				return i
	return -1

"""Read the complete file and insert each value into 
an array"""
def read_from_file(in_filename: str):
    output_buffer = []
    with open(in_filename, 'r') as number_file:
        for current_line in number_file:
            output_buffer.append(int(current_line.strip()))

    return output_buffer

# =========================================

if len(sys.argv) < 2:
    print("Usage: linear_search   number")
    sys.exit(0)

number = int(sys.argv[1])

an_array = read_from_file("user_data.csv")

start_time = time.perf_counter()
result = linear_search(an_array, number)
end_time = time.perf_counter()

print("Result: ", result)
print("Processing time:    ", (end_time - start_time), " secs")