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
    pivotValue = array[left]
    i = left + 1
    for j in range(left+1, right+1):
        if array[j] < pivotValue:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i = i+1
    temp = array[left]
    array[left] = array[i-1]
    array[i-1] = temp
    return i-1


file_handle = open("maininput.txt", "r")
array = []
for line in file_handle:
    array.append(int(line.strip("\r\n")))

print "length of the array is ", len(array)

"""
array = [i for i in range(1,101)]
"""
"""
array = [2,8,9,3,7,5,10,1,6,4]
"""
print quicksort(array, 0, len(array) - 1) 

print comparisons
