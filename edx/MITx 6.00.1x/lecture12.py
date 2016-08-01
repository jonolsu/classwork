import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name

# me = Person("William Eric Grimson")
# print me
# foo = 'William Eric Grimson'
# foo.split(' ')
# foo.split(' ')[-1]
# me.getLastName()
#
# me.setBirthday(1,2,1927)
# me.getAge()
#
# her = Person("Cher")
# her.getLastName()
# plist = [me, her]
# for p in plist: print p
# twin = Person("Eric William Grimson")
# plist.sort()
# plist = [me, her, twin]
# for p in plist: print p
# plist.sort()
# for p in plist: print p

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign, belongs to class (not instances)

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(MITPerson):
    pass
    
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year

class Grad(Student):
    pass

class TransferStudent(MITPerson):
    pass

def isStudent(obj):
    return(isinstance(obj,Student))


# p1 = MITPerson('Eric')
# p2 = MITPerson('John')
# p3 = MITPerson('John')
# p4 = Person('John')

# print p1
# p1.getIdNum()
# p2.getIdNum()
# p1 < p2
# p3 < p2
# p4 < p1

# p1 < p4 #will be error

# s1 = UG('Fred', 2016)
# s2 = Grad('Angela')
# isStudent(s1)
# isStudent(s2)
# me = MITPerson('Eric')
# isStudent(me)

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print self.incantation    


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())




class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print "A.x"
    def y(self):
        print "A.y"
    def z(self):
        print "A.z"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print "B.y"
    def z(self):
        print "B.z"

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print "C.y"
    def z(self):
        print "C.z"

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print "D.z"
        
# obj = D()
# print obj.a
# print obj.b
# print obj.c
# print obj.d
# print obj.x()
# print obj.y()
# print obj.z()

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = [] # list of Student objects
        self.grades = {} # maps idNum -> list of grades
        self.isSorted = True # true if self.students is sorted
    
    def addStudent(self, student):
        """Assumes: student is of the type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student no in the grade book')
        
    def getGrades(self, student):
        """Return a list of grades for student"""
        try: #return copy of student's grades
            return self.grades[student.getIdNum()][:] #return a copy, not the original so it can't be messed up
        except KeyError:
            raise ValueError('Student no in grade book')
    
    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        #return self.students[:]  #returns a of list of students
        for s in self.students:
            yield s #use a generator function instead
    
def gradeReport(course):
    """Assumes: course is of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot+=g
            numGrades +=1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + 'has no grades')
    return '\n'.join(report)

# ug1 = UG('Jane Doe',2014)
# ug2 = UG('John Doe',2015)
# ug3 = UG('David Henry',2003)
# g1 = Grad('John Henry')
# g2 = Grad('George Steinbrenner')

# six00 = Grades()
# six00.addStudent(g1)
# six00.addStudent(ug2)
# six00.addStudent(ug1)
# six00.addStudent(g2)

# for s in six00.allStudents():
#     six00.addGrade(s, 75)
# six00.addGrade(g1, 100)
# six00.addGrade(g2, 25)

# six00.addStudent(ug3)

# print(gradeReport(six00))

# for s in six00.allStudents():
#    print s
# for s in six00.students: # this method voilates abstraction
#     print s


def genTest():
    yield 1
    yield 2
# foo = genTest()
# foo.next()
# foo.next()
# foo.next()

# generator for the Fibonacci sequence
def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

# fib = genFib()
# fib
# fib.next()
# fib.next()
# fib.next()
# fib.next()
# for n in genFib():
#     print n

def genPrimes():
    firstpass = True
    while True:
        if firstpass:
            firstpass = False
            foundPrime = True
            primeNums = [2]
            currentNumber = 2
        else:
            currentNumber +=1
            foundPrime = True
            for p in primeNums:
                if (currentNumber % p) == 0:
                    foundPrime = False
        if foundPrime:
            primeNums.append(currentNumber)
            yield currentNumber
        
# a = genPrimes()
# a.next()
# a.next()
# a.next()
        