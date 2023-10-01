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


#HYBRID SORT & COUNTER
def hybridmerge(l, r):  # L and R are the arrays aka to be merged
    global hybridcom
    merged = []
    i = j = 0
    while i < len(l) and j < len(r):
        hybridcom += 1
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

def hybridinsertsort(ar):
    global hybridcom
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
            hybridcom += 1 # increment number of comparisons
        
        # Place key at after the element just smaller than it.
        ar[stepcount + 1] = key

    return ar # return sorted array
def hybridsort(ar,s):
    if len(ar) > s:
        mid = len(ar) // 2
        left = ar[:mid]
        right = ar[mid:]
        leftDone = hybridsort(left,s)
        rightDone = hybridsort(right,s)
        result = hybridmerge(leftDone, rightDone)
    else:
        result=hybridinsertsort(ar)

    return result

# helper function to print a list
def printer(array):
    for i in range(len(arr)):
        print(array[i], end=" ")
    print()


if __name__ == "__main__":
    n = 10000000
    s = 6
    print("Started")
    arr = [random.randrange(1, n, 1) for i in range(n)]
    insertmergearr = copy.copy(arr)

    # Merge Sort
    mergedcom = 0
    start = time.time()
    mergeSortedArray = mergesort(copy.copy(arr))
    end = time.time()
    mergeSortTime = end - start
    mergeSortComparisons = mergedcom

    print("Finished merge")
   # Hybrid Sort
    hybridcom = 0
    start = time.time()
    hybridSortedArray = hybridsort(copy.copy(insertmergearr), s)
    end = time.time()
    hybridSortTime = end - start
    hybridSortComparisons = hybridcom

    print(f"Array Size={n}, s={s}")
    print("Merge Sort Time:", mergeSortTime, "seconds")
    print("Merge Sort Comparisons:", mergeSortComparisons)
    print("Hybrid Sort Time:", hybridSortTime, "seconds")
    print("Hybrid Sort Comparisons:", hybridSortComparisons)