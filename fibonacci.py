import sys
import random
import time

def fibonacci_recursive(n):
    # Check if input is correct
    if n < 0:
        print("Incorrect input")

    # Check if n is 0 then it will return 0
    elif n == 0:
        return 0
    
    # Check if n is 1,2 it will return 1
    elif n == 1 or n == 2:
        return 1

    else:       
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Function for nth fibonacci number 
def fibonacci_loop(n):
    a = 0
    b = 1
    
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
        
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
      
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# =========================================

if len(sys.argv) < 2:
    print("Usage: fibonacci_recursion    number")
    # sys.exit(0)

    print("Selecting a random number between 1 and 50")
    num = random.randint(1,50)

else:
    num = int(sys.argv[1])

start_time = time.perf_counter()
result = fibonacci_recursive(num)
end_time = time.perf_counter()

print("Fibonacci value:    ", result)
print("Number iterations:  ", num)
print("Processing time:    ", (end_time - start_time), " secs")





start_time = time.perf_counter()
result = fibonacci_loop(num)
end_time = time.perf_counter()

print("Fibonacci value:    ", result)
print("Number iterations:  ", num)
print("Processing time:    ", (end_time - start_time), " secs")