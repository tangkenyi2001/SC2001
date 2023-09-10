import random
import time
# from tkinter import *
import numpy as np # verify is list is sorted

# global variable that tracks key comparisons
com = 0


# merge function
def merge(l, r):  # L and R are the arrays aka to be merged
    global com
    merged = []
    i = j = 0
    while i < len(l) and j < len(r):
        com += 1
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


# mergeSort function
def mergesort(ar):
    global com
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

# insertionSort function
# Source: https://www.programiz.com/dsa/insertion-sort#google_vignette
def insertsort(ar):
    global com

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
            com += 1 # increment number of comparisons
        
        # Place key at after the element just smaller than it.
        ar[stepcount + 1] = key

    return ar # return sorted array

# mergeSort function designed to work with insertion sort
# DISCLAIMER: I DID THIS WITH CHATGPT AND GOOGLING IDK IF ITS CORRECT
# I am pretty sure there is something wrong with this function because it is almost the same as mergesort...
def mergesort_adjusted(ar, threshold):
    global com
    if len(ar) > threshold:
        mid = len(ar) // 2
        left_half = ar[:mid]
        right_half = ar[mid:]

        mergesort_adjusted(left_half, threshold)
        mergesort_adjusted(right_half, threshold)

        left_index = right_index = current_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                ar[current_index] = left_half[left_index]
                left_index += 1
            else:
                ar[current_index] = right_half[right_index]
                right_index += 1
            current_index += 1
            com += 1

        while left_index < len(left_half):
            ar[current_index] = left_half[left_index]
            left_index += 1
            current_index += 1

        while right_index < len(right_half):
            ar[current_index] = right_half[right_index]
            right_index += 1
            current_index += 1
    else:
        insertsort(ar) #default back to insertsort if array is small enough

    return ar
    
# hybrid sort here
def hybridSort(ar, threshold):
    if len(ar) <= threshold: # if array is small enough, use insertion sort, trivial case
        insertsort(ar)
    else:
        mergesort_adjusted(ar, threshold) # else use merge sort

    return ar


# helper function to print a list
def printer(array):
    for i in range(len(arr)):
        print(array[i], end=" ")
    print()


if __name__ == "__main__":  # main function
    # for S in range(9, 16, 1):
    mergeArray = []  # Sorted Array for Merge Sort
    insertArray = [] # Sorted Array for Insertion Sort
    hybridArray = [] # Sorted Array for Hybrid Sort
    com = 0
    
    # change n to change size of array
    n = 10000

    # set threshold size S for switching to insertion sort
    threshold = 8

    arr = [random.randrange(1, n, 1) for i in range(n)]  # list comprehension
    start = time.time()
    mergeArray = mergesort(arr)
    print("MergeSort sorted array within", time.time() - start, "seconds")
    # printer(mergeArray) # print at your own risk
    print("MergeSort made", com, "key comparisons")

    # start = time.time() # reset timer
    # com = 0 # reset comparisons

    # BEWARE: insertsort is slow for large arrays THIS COULD TAKE A WHILE, COMMENT OUT IF NECESSARY
    # insertArray = insertsort(arr)
    # print("InsertSort sorted array within", time.time() - start, "seconds")
    # print("InsertSort made", com, "key comparisons")

    start = time.time() # reset timer
    com = 0 # reset comparisons

    hybridArray = hybridSort(arr, threshold)
    print("hybridSort sorted array within", time.time() - start, "seconds")
    print("hybridSort made", com, "key comparisons")


    # Source: https://www.geeksforgeeks.org/python-check-if-list-is-sorted-or-not/
    # this tests all differences between consecutive elements in the array to that they are all positive (ascending order)
    # Feel free to comment away for faster runtime if necessary
    # Also this will return true for an empty array, so take note of that
    test_arr = np.array(mergeArray)

    if np.all(np.diff(test_arr) >= 0):
        print("Yes, MergeArray is sorted.")
    else:
        print("No, MergeArray is not sorted.")

    test_arr = np.array(insertArray)

    if np.all(np.diff(test_arr) >= 0):
        print("Yes, InsertArray is sorted.")
    else:
        print("No, InsertArray is not sorted.")

    test_arr = np.array(hybridArray)

    if np.all(np.diff(test_arr) >= 0):
        print("Yes, hybridArray is sorted.")
    else:
        print("No, hybridArray is not sorted.")

