#Problem Set 1

def prob1(s):
    numvowels = 0
    for letter in s:
        if letter in ('a','e','i','o','u'):
            numvowels+=1
    print "Number of vowels:",numvowels

def prob2(s):
    numbobs = 0
    for i in range(0,len(s)):
        if i < len(s)-2:
            if(s[i] == "b" and s[i+1] == "o" and s[i+2] == "b"):
                numbobs+=1
    print "Number of times bob occurs is:",numbobs            

def item_order(order):
    numsalads = order.count("salad")
    numhamburger = order.count("hamburger")
    numwater = order.count("water")
    return("salad:"+str(numsalads)+" hamburger:"+str(numhamburger)+" water:"+str(numwater))

#Problem Set 2

def prob1(balance,annualInterestRate,monthlyPaymentRate):
    newbalance = round(float(balance),2)
    totalpaid = 0.0
    for i in range(1,13):
        minpayment = round(float(monthlyPaymentRate)*newbalance,2)
        interest = round((newbalance-minpayment)*(annualInterestRate/12),2)
        newbalance = round(newbalance - minpayment + interest,2)
        print "Month:",i
        print "Minimum monthly payment:",minpayment
        print "Remaining balance:",newbalance
        totalpaid += minpayment
    print "Total paid:",totalpaid
    print "Remaining balance:",newbalance
    
def prob2(balance,annualInterestRate):
    def finalbalance(balance,annualInterestRate,monthlyPayment):
        newbalance = round(float(balance),2)
        totalpaid = 0.0
        for i in range(1,13):
            interest = round((newbalance-monthlyPayment)*(annualInterestRate/12),2)
            newbalance = round(newbalance - monthlyPayment + interest,2)
        return (newbalance)
    guess=0
    left = finalbalance(balance,annualInterestRate, guess)
    while(left > 0):
        oldguess = guess
        guess = guess + 10
        left = finalbalance(balance,annualInterestRate, guess)
    print"Lowest Payment:",guess 
    
def prob3(balance,annualInterestRate):
    def finalbalance(balance,annualInterestRate,monthlyPayment):
        newbalance = round(float(balance),2)
        totalpaid = 0.0
        for i in range(1,13):
            interest = round((newbalance-monthlyPayment)*(annualInterestRate/12),2)
            newbalance = round(newbalance - monthlyPayment + interest,2)
        return (newbalance)
    lowguess=balance/12
    highguess=(balance * (1 + annualInterestRate/12)**12) / 12.0
    midguess=round((lowguess+highguess)/2,2)
    left = finalbalance(balance,annualInterestRate, midguess)
    while(highguess-lowguess>.02 or left==0):
        if(left>0):
            lowguess=round(midguess,2)
        else:
            highguess=round(midguess,2)
        midguess=round((lowguess+highguess)/2,2)

        left = finalbalance(balance,annualInterestRate, midguess)
    print"Lowest Payment:",highguess 

#Problem Set 3
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
    the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
    between start and stop times.
    '''
    interim = start
    cumexposure = 0
    while interim < stop:
        cumexposure = cumexposure + f(interim)*step
        interim += step
    return cumexposure
