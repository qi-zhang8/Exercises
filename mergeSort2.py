
def merge(L,R):
    if len(L) == 0:
        return R
    elif len(R) == 0:
        return L
    else:
        if L[0] <= R[0]:
            first = L[0]
            rest = merge(L[1:], R)
        else:
            first = R[0]
            rest = merge(L, R[1:])
        return [first]+rest

def merge_sort(A):
    if len(A) == 1:
        return A
    middle = len(A)/2
    
    L = merge_sort(A[0:middle])
    R = merge_sort(A[middle:])

    return merge(L,R)

def test(testInputs):
    Result = []
    for testIn in testInputs:
        print("Before:", testIn)
        result = merge_sort(testIn)
        print("After:", result)

A = [1,6,3,6,2,7,8,4,9,11]
AA = [1,3,5,7,9,2,4,6,8,10]
B = [1,3,2,4,5,7,8,2,10]
C = [1,2,3,4,5,6,7,8,9]
D = [9,8,7,6,5,4,3,3,1]
E = [1,1,1,1,1,1,1,1,1]

test([A,AA,B,C,D,E])

