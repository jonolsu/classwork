def dict_invert(d):
    dinv = {}
    for item in d:
        if(dinv.get(d.get(item))):
            templist = dinv.get(d.get(item))
            dinv.pop(d.get(item))
            tempinsert = []
            for titem in templist:
                tempinsert.insert(0,titem)
            tempinsert.insert(0,item)
            tempinsert.sort()
            dinv[d.get(item)] = tempinsert
        else:
            dinv[d.get(item)] = [item]
    return dinv

def getSublists(L, n):
    sublist = []
    for i in range(len(L)):
        if len(L)-n-i >=0:
            sublist.append(L[i:i+n])
    return sublist
    
def longestRun(L):
    longestsofar = 1
    for i in range(len(L)):
        j=1
        stillok = True
        while(stillok and i+j < len(L)):
            if L[i+j-1] <= L[i+j]:
                j+=1
            else:
                stillok = False
        longestsofar = max(longestsofar,j)
    return longestsofar
    
## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status in ('citizen','legal_resident','illegal_resident'):
            self.status = status
        else:
            raise ValueError
            
    def getStatus(self):
        """
        Returns the status
        """
        return self.status

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)
        
class ArrogantProfessor(Professor): 
        
    def lecture(self, stuff):
        return "It is obvious that I believe that " + Person.say(self, stuff)
                
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

#6.2
print('ae.say()')
print(ae.say('the sky is blue'))
print('eric says: It is obvious that I believe that eric says: the sky is blue')
print('ae.lecture()')
print(ae.lecture('the sky is blue'))
print('It is obvious that I believe that eric says: the sky is blue')
print

class Professor(Lecturer): 
    def say(self, stuff): 
        return "Prof. " + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
        
    def lecture(self, stuff):
        return "It is obvious that I believe that " + Person.say(self, stuff)

pe = Professor('eric') 
ae = ArrogantProfessor('eric')

#6.3
print('pe.say()')
print(pe.say('the sky is blue'))
print('Prof. eric says: I believe that eric says: the sky is blue ')
print('ae.say()')
print(ae.say('the sky is blue'))
print('Prof. eric says: It is obvious that I believe that eric says: the sky is blue')
