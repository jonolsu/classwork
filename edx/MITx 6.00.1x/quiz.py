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

def f(a,b):
    return a+b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = list(set(d1.keys()) & set(d2.keys()))
    intervalue = {}
    for i in intersect:
        intervalue[i] = f(d1[i],d2[i])

    
    diffvalue = {}
    difference = list(set(d1.keys()).symmetric_difference(set(d2.keys())))
    for d in difference:
        if d in d1:
            diffvalue[d] = d1[d]
        else:
            diffvalue[d] = d2[d]

    return intervalue, diffvalue

def f(s):
    return 'a' in s
        
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    newL = L[:]
    for s in newL:
        if not isinstance(s,str):
            L.remove(s)
        elif not (f(s)):
            L.remove(s)
    return (len(L))

#run_satisfiesF(L, satisfiesF)
      
#L = ['a', 'b', 'a']
#print satisfiesF(L)
#print L

