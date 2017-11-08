
def perm(s, length):
    if len(s) == 1:
        return [s]
    result = []
    for i in range(0, len(s)):
        firstChar = s[i]
        if (i == 0):
            left = ''
        else:
            left = s[0:i]
        right = s[i+1:len(s)]
        rest = left + right
        subResult = perm(rest, length)
        for sub in subResult:
            resultStr = firstChar + sub
            result.append(resultStr)
            if len(resultStr) == length:
                print firstChar+sub
    return result

strList = perm('abc', 3)
#for s in strList:
#    print s
