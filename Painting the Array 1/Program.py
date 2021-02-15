import time
import os
import psutil

# Method that optimally separates an array a in 2 arrays
def separate(a):
    newLst = []
    i = 1
    ourLen = len(a)
    while i < ourLen:
        if a[i - 1] == a[i] and not a[i] in newLst:
            newLst.append(a[i])
            del a[i]
            ourLen -= 1
        else:
            i += 1

    return a, newLst


# Method that calculates the segments of an array
def seg(a):
    i = 1
    ourLen = len(a)
    while i < ourLen:
        if a[i - 1] == a[i]:
            del a[i]
            ourLen -= 1
        else:
            i += 1

    return len(a)


# Read first line - an integer n,  1 <= n <= 100000
print("Type an integer value n, 1 <= n <= 100000.")
n = 0
while n < 1 or n > 100000:
    n = int(input("n = "))

# Read the second line - n integers a1,a2,…,an, 1 <= ai <= n
print("Type n integers a separated by whitespace, 1 <= ai <= n ")
lst = [int(i) for i in input("Array = ").split(" ")]

# Check the input
if len(lst) != n:
    print("Wrong array input!")
    exit()
for i in lst:
    if i < 1 or i > n:
        print("Wrong array input!")
        exit()

# Start the timer
start_time = time.time()

# Prepare the output - the maximal possible total number of segments
lst, newLst = separate(lst)
print(f"Output: {seg(lst) + seg(newLst)}")

# Stop the timer
print(f"\nExecution Time: {time.time() - start_time} ms")

# Memory used
process = psutil.Process(os.getpid())
mem = process.memory_info().rss
print(f"Memory used: {mem} bytes = {mem / 1000000} megabytes")