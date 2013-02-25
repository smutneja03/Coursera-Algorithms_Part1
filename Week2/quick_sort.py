#!/usr/bin/python
import math
comparisons = 0
def quicksort(array, left, right):
    global comparisons
    if left < right:
        #Get lists of bigger and smaller items and final position of pivot
        comparisons+=right-left
        pivotNewIndex = partition(array, left, right)
        #Recursively sort elements smaller than the pivot
        quicksort(array, left, pivotNewIndex-1)
        #Recursively sort elements at least as big as the pivot
        quicksort(array, pivotNewIndex + 1, right)
        return array

#left is the index of the leftmost element of the array
#right is the index of the rightmost element of the array (inclusive)
#number of elements in subarray = right-left+1
def partition(array, left, right):
    global comparisons
    pivotindex = int(math.ceil((right+1+left)/2)) - 1
    pivotValue = array[pivotindex]
    i = left
    for j in range(left, right+1):
        if array[j] < pivotValue:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i = i+1
    temp = array[array.index(pivotValue)]
    array[array.index(pivotValue)] = array[i]
    array[i] = temp
    return i


file_handle = open("input.txt", "r")
array = []
for line in file_handle:
    array.append(int(line.strip("\r\n")))

print "length of the array is ", len(array)

"""
array = [i for i in range(1,11)]
"""
"""
array = [2,8,9,3,7,5,10,1,6,4]
"""
print quicksort(array, 0, len(array) - 1) 

print comparisons
