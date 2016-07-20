class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ', ' + str(self.y) + ')'
        
#a=Coordinate(10,20)
#print(a)
#repr(a)


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        return len(self.vals)

    def intersect(self, other):
        """Returns the intersect set"""
        returnset = intSet()
        for o in other.vals:
            if self.member(o):
                returnset.insert(o)
        return returnset

# s = intSet()
# print s
# s.insert(3)
# s.insert(4)
# s.insert(3)
# print s
# s.member(3)
# s.member(5)
# s.insert(6)
# print s
# s.remove(3)
# print s
# s.remove(3)

# a = intSet()
# a.insert(1)
# a.insert(2)
# a.insert(3)
# b = intSet()
# b.insert(2)
# b.insert(3)
# b.insert(4)
# c = a.intersect(b)
# len(c)

class Queue(object):
    
    def __init__(self):
        self.vals = []
    def insert(self,e):
        self.vals = [e] + self.vals
    def remove(self):
        try:
            return self.vals.pop()
        except:
            raise ValueError()
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

# q = Queue()
# q.insert(1)
# q.insert(-20)
# q.insert(200)
# print(q)
# print(q.remove())
# print(q)
# print(q.remove())
# print(q)
            
