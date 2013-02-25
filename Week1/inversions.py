inversions = 0
file_handle = open("input.txt", "r")
array = []
for line in file_handle:
    array.append(int(line.strip("\r\n")))

print "length of the array is ", len(array)

def merge(left, right):
    global inversions
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1           
        else:
            result.append(right[j])
            inversions += len(left) - i
            j += 1
#   print "result of the array before", result
    result += left[i:]
    result += right[j:]
#   print "result of the array is ", result
    return result
 
 
def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = int( len(lst) / 2 )
    left = mergesort(lst[:middle])
#   print "left part of the main array after left mergesort is ", left
    right = mergesort(lst[middle:])
#   print "right part of the main array after right mergesort is ", right
    return merge(left, right)


print mergesort(array)
print "number of inversions in the array---->",inversions
