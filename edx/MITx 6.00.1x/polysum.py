import math
# math module contains convenience functions for calculating polysum

def polysum(n,s):
    """ Returns the area plus the square of the perimeter
    for a regular polygon, where n = the number of sides
    and s = the length of each side, rounded to four decimal places """
    
    area = (.25*n*s*s)/math.tan(math.pi/n)
    perimeter = s*n
    returnval = area+perimeter**2.0
    returnval = round(returnval,4)
    return(returnval)