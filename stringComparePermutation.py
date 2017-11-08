
def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)
    if sortedStr1 == sortedStr2:
        return True

def test(str1, str2):
    print str1, str2
    print isPermutation(str1, str2)

A = "abcdefg"
B = "bcdeafg"
C = "abc def"
D = "defabc "

test(A,B)
test(C,D)
