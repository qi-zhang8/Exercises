
def binarySearch(list, value):
    listLen = len(list)
    begin = 0
    end = listLen
    for i in range(begin,end):
        middleIndex = (end-begin)/2 + begin
        if list[middleIndex] == value:
            return middleIndex
        elif list[middleIndex] > value:
            end = middleIndex
        elif list[middleIndex] < value:
            begin = middleIndex
    return -1

def test(list, value):
    print list, value
    print binarySearch(list, value)

A = [1,2,3,4,5,6,7,8,9,10]

test(A, 5)
test(A, -1)
test(A, 11)
