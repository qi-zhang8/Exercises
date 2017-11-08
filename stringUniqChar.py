
def isUniqueChar(myStr):
    for i in range(len(myStr)-1):
        for j in range (i+1, len(myStr)):
            if myStr[i] == myStr[j]:
                return False
    return True

def test(myStr):
    print myStr
    print isUniqueChar(myStr)

A = "abcdefg"
B = "aaaaaaa"
C = "abcdefa"
D = "a b c d ab"

test(A)
test(B)
test(C)
test(D)
