#!/usr/bin/python
import math
comparisons = 0
def randomised(array, left, right):
    middle = array[int(math.floor((left+right)/2))]
    pivotindex = array.index(sorted([ array[left], array[right], middle ])[1])
    temp = array[pivotindex]
    array[pivotindex] = array[left]
    array[left] = temp
    return partition(array, left, right)


def quicksort(array, left, right):
    global comparisons
    if left< right:
        #Get lists of bigger and smaller items and final position of pivot
        comparisons+=right-left
        pivotNewIndex = randomised(array, left, right)
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
    i = left+1
    for j in range(left+1, right+1):
        if array[j] < pivotValue:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
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

#array = [1, 11, 5, 15, 2, 999, 3, 2, 98, 765, 8, 14, 15, 16, 88, 145, 100, 12, 9, 99, 77, 0]

"""

array = [i for i in range(1,101)]
"""

"""
array = [2,8,9,3,7,5,10,1,6,4]
"""
print quicksort(array, 0, len(array) - 1) 

print comparisons
