import os
import sys
import time
import random

from math import sqrt

# prime function to check given number prime or not
def Prime(number, itr):  
    # base condition
    if itr == 1 or itr == 2:  
        return True
      # if given number divided by itr or not
    if number % itr == 0:  
        return False
      # Recursive function Call
    if Prime(number, itr - 1) == False:  
        return False

    return True


# =========================================

if len(sys.argv) < 2:
    # print("Usage: prime_recursion   number")
    # sys.exit(0)
    num = random.randint(1,1000000)

else:
    num = int(sys.argv[1])


itr = int(sqrt(num) + 1)

start_time = time.perf_counter()
result = Prime(num, itr)
end_time = time.perf_counter()

print("Number:          ", num, " is  Prime: ", result)
print("Processing time: ", (end_time - start_time))
