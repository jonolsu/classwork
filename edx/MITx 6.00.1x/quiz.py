def isPalindrome(aString):
    '''
    aString: a string
    '''
    returnvalue=True
    for i in range(len(aString)):
        returnvalue = returnvalue and (aString[i] == aString[-i-1])
    return returnvalue
    
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    runningsum = 0
    for i in range(len(listA)):
        runningsum += (listA[i]*listB[i])
    return runningsum

def flatten(aList):
    if aList == []:
        return aList
    if isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])
            

            