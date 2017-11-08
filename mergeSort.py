
def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(0,n1):
        L.append(A[p+i])
    for j in range(0,n2):
        R.append(A[q+1+j])

    i = 0
    j = 0
    for k in range(p, r+1):
        if (i < n1 and j < n2 and L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        elif (i < n1 and j < n2 and L[i] > R[j]):
            A[k] = R[j]
            j += 1
        elif (i >= n1 and j < n2):
            A[k] = R[j]
            j += 1
        elif (j >= n2 and i < n1):
            A[k] = L[i]
            i += 1

def merge_sort(A, p, r):
    if p < r:
        q = (r+p)/2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def test(testInputs):
    for testIn in testInputs:
        print("Before:", testIn)
        merge_sort(testIn, 0, len(testIn)-1)
        print("After:", testIn)

A = [1,6,3,6,2,7,8,4,9,11]
AA = [1,3,5,7,9,2,4,6,8,10]
B = [1,3,2,4,5,7,8,2,10]
C = [1,2,3,4,5,6,7,8,9]
D = [9,8,7,6,5,4,3,3,1]
E = [1,1,1,1,1,1,1,1,1]

test([A,AA,B,C,D,E])

