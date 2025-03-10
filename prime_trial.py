import time
import os
import sys
import random

def is_prime_trial_division(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            return False

    return True


def prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime_trial_division(num):
            primes.append(num)
    return primes

# =========================================

if len(sys.argv) < 3:
    # print("Usage: prime_recursion   start    end")
    # sys.exit(0)
    start_interval = random.randint(1,1000)
    end_interval = random.randint(1,1000000)
else:
    start_interval = int(sys.argv[1])
    end_interval = int(sys.argv[2])

start_time = time.perf_counter()

list_numbers = prime_numbers_in_range(start_interval, end_interval)  

end_time = time.perf_counter()

print("Range:            ", start_interval, ", ", end_interval)
print("Number of primes: ", len(list_numbers))
print("Size:             ", (len(list_numbers) * sys.getsizeof(int))/1024, " Kilobytes")

print(f"Processing time: {(end_time - start_time) } secs")
