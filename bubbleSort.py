def bubbleSort(list):
    swapped = False
    listLen = len(list)
    for i in range(listLen-1):
        for j in range(listLen-1-i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                swapped = True
        if swapped == False:
            print "No swap"
            break

def test(list):
    bubbleSort(list)
    print list

A = [1,2,3,4,5,6,7,8,9]
B = [9,8,7,6,5,4,3,2,1,0]
C = [1,1,1,1,1,1,1,1,1,1]
D = [1,4,5,6,2,3,5,8,9,10]

test(A)
test(B)
test(C)
test(D)
