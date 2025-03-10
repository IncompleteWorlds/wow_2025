import sys
import random
import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    return arr


# =========================================

if len(sys.argv) < 2:
    print("Usage: bubble_sort   file")
    # sys.exit(0)

    # print("Selecting a random number between 1 and 50")
    # num = random.randint(1,50)

    data_buffer = None

else:
    filename = int(sys.argv[1])

    with open(filename, "r") as f:
        data_buffer = f.read()

start_time = time.perf_counter()
result = insertion_sort(data_buffer)
end_time = time.perf_counter()

print("Input array:    ", data_buffer)
print("Memory: ")
print("Processing time:    ", (end_time - start_time), " secs")