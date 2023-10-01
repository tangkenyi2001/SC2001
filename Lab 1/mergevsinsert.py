import matplotlib.pyplot as plt
import numpy as np
import random
import time
import copy
import math


# global variable that tracks key comparisons

mergedcom=0
hybridcom = 0
insertcom=0
s= 0 #threshhold number
# merge function
#MERGESORT FUNCTION
def mergesort(ar):
    global mergedcom
    if len(ar) > 1:
        mid = len(ar) // 2
        left = ar[:mid]
        right = ar[mid:]
        leftDone = mergesort(left)
        rightDone = mergesort(right)
        result = merge(leftDone, rightDone)
    else:
        result = ar

    return result
#Comparison Counter for pure mergesort
def merge(l, r):  # L and R are the arrays aka to be merged
    global mergedcom
    merged = []
    i = j = 0
    while i < len(l) and j < len(r):
        mergedcom += 1
        if l[i] < r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1

    while i < len(l):
        merged.append(l[i])
        i += 1

    while j < len(r):
        merged.append(r[j])
        j += 1

    return merged

#Comparison Counter for pure insertion sort
def insertsort(ar):
    global insertcom
    # Trivial case: array of length 1 is already sorted
    if len(ar) == 1: return ar # return sorted array

    for step in range(1, len(ar)):
        key = ar[step]   # Set first element to be comparison key in unsorted array
        stepcount = step - 1 # decrement number of steps needed to traverse entire array
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while stepcount >= 0 and key < ar[stepcount]:
            ar[stepcount + 1] = ar[stepcount]
            stepcount -= 1
            insertcom += 1 # increment number of comparisons
        
        # Place key at after the element just smaller than it.
        ar[stepcount + 1] = key

    return ar # return sorted array
if __name__ == "__main__":
    array_sizes = list(range(1, 30))  # Array sizes from 2 to 100
    merge_comparisons = []
    insert_comparisons = []

    for n in array_sizes:
        # Generate a random array of size n
        arr = [random.randrange(1, n * 10, 1) for i in range(n)]

        # Merge Sort
        mergedcom = 0
        mergesort(copy.copy(arr))
        merge_comparisons.append(mergedcom)

        # Insertion Sort
        insertcom = 0
        insertsort(copy.copy(arr))
        insert_comparisons.append(insertcom)

    # Plot comparison data
    plt.figure(figsize=(12, 8))
    plt.title("Comparisons vs. Array Size")
    plt.plot(array_sizes, merge_comparisons, label='Merge Sort', color='blue')
    plt.plot(array_sizes, insert_comparisons, label='Insertion Sort', color='red')
    plt.xlabel('Array Size')
    plt.ylabel('Number Of Key Comparisons')
    plt.legend()
    plt.show()