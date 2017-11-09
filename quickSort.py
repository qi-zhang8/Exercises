def quicksort(array, begin, end):
    if begin < end:
        pIndex = partition(array, begin, end)
        quicksort(array, begin, pIndex)
        quicksort(array, pIndex+1, end)
    return array

def swap(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp
    
def partition(array, begin, end):
    assert(begin<end)
    if end-begin == 1:
        return begin

    pIndex = end-1
    i = begin
    while i < pIndex:
        if pIndex == i+1:
            if array[i] > array[pIndex]:
                swap(array, i, pIndex)
                return i
            else:
                return pIndex
        if array[i] > array[pIndex]:
            swap(array, pIndex-1, pIndex)
            swap(array, i, pIndex)
            pIndex = pIndex - 1
        else:
            i += 1
    return pIndex
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print quicksort(test, 0, len(test))
