import random
import time

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

# insertion sort here


# hybrid sort here


# helper function to print a list
def printer(array):
    for i in range(len(arr)):
        print(array[i], end=" ")
    print()


if __name__ == "__main__":  # main function
    # for S in range(9, 16, 1):
    mergeArray = []
    # hybridArray = []
    com = 0
    n = 200
    arr = [random.randrange(1, n, 1) for i in range(n)]  # list comprehension
    start = time.time()
    mergeArray = mergesort(arr)
    print("MergeSort sorted array within", time.time() - start, "seconds")
    # printer(mergeArray) # print at your own risk
    print("MergeSort made", com, "key comparisons")
