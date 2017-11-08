
def isUniqueChar(myStr):
    myDict = dict()
    for i in range(len(myStr)):
        if myStr[i] in myDict:
            return False
        else:
           myDict[myStr[i]] = myStr[i]
    return True

def test(myStr):
    print myStr, isUniqueChar(myStr)

A = "abcdefg"
B = "aaaaaaa"
C = "ab cd ef g a"
D = "abcddeeff"

test(A)
test(B)
test(C)
test(D)
