
def isPalindrome(str):
    spaceCount = 0
    myDict = dict()
    for i in range(len(str)):
        if str[i] == ' ':
            spaceCount += 1
        elif str[i] in myDict:
           myDict[str[i]] += 1
        else:
           myDict[str[i]] = 1

    foundOneSingle = False
    for key in myDict:
        value = myDict[key]
        if value % 2 != 0 and (len(str)-spaceCount) % 2 == 0:
            return False
        elif value % 2 != 0 and foundOneSingle == False:
            foundOneSingle = True
        elif value % 2 != 0 and foundOneSingle == True:
            return False
    return True

def test(str):
    print str
    print isPalindrome(str)

A = "race car"
B = "abc cba"
C = "abcdefg"
D = "abcdefgh"

test(A)
test(B)
test(C)
test(D)
