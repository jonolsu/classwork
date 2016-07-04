def ndigits(x):
    '''
    takes an integer x (either positive or negative) as an
    argument and returns the number of digits in x. Implemented
    by recursively performing integer division by 10 and exiting
    when the result of the division is zero (meaning a single
    digit number)
 
    x: integer (either positive or negative)

    returns: an integer representing the number of digits in x
    '''
    if abs(x) / 10 == 0:
        return 1
    else:
        return 1 + ndigits(abs(x)/10)
