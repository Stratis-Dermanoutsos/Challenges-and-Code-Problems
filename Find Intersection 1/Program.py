import json
import os
import psutil
import time


# Method that finds an intersection, if one exists
def FindIntersection(strArr):
    strArr = json.loads(strArr)
    arr1 = [int(x) for x in strArr[0].split(",")]
    arr2 = [int(x) for x in strArr[1].split(",")]

    result = [x for x in arr1 if x in arr2]

    if len(result) > 0:
        return result

    return "false"


# Get the input
myArr = input("Type an array of 2 strings, each containing any number of integer values sorted in ascending order:\n")

# Start the timer
start_time = time.time()

# Prepare the output - the intersection, if there is one
myResult = FindIntersection(myArr)
print(f"Output: {myResult}")

# Stop the timer
print(f"\nExecution Time: {time.time() - start_time} ms")

# Memory used
process = psutil.Process(os.getpid())
mem = process.memory_info().rss
print(f"Memory used: {mem} bytes = {mem / 1000000} megabytes")