"""
check list is mutable in python
"""
my_list = [1, 2, 3, 4, 5]
print('Bo nho luu lai array o day:', id([1, 2, 3, 4, 5]))
print( 'Bo nho luu my_list o day:', id(my_list))
change_list = my_list
change_list[0] = -1
print('After change value in array:')
print(my_list)
print(id(my_list), id(change_list))
print('Bo nho luu lai array o day:', id([1, 2, 3, 4, 5]))
"""
check tuple is mutable in python
"""
my_tuple = (1, 2, 3)
change_tuple = my_tuple
print(id(my_tuple), id((1, 2, 3)))
print(my_tuple)
"""
Example for mutable and immutable object in python
"""
print('=================')
x=10
y=x
print(id(x)==id(y)) #True
print(id(x)==id(10)) #True
x = x+1
print(id(x),id(10))
print(id(x),id(y))
"""
that mean object 10=int never modified!!!
immiutable objects dosent allow modification after creation
"""
m = list([1, 2, 3])
print([1,2,3])
n = m
print(id(m), id(n), id([1,2,3]))
m.pop()
print(id(m), id(n), id([1,2]))

"""
link : https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747
"""


"""
coppy object
"""
class Point:
    """
    Point in 2D.
    attributes: x, y.
    """
    def __init__(self, x, y):
        self.x =x
        self.y =y

    def showInfo(self):
        print(self.x, self.y)
        print('id:',id(self))
import copy
p1 = Point(3, 4)
print(p1.x)
p2 = copy.copy(p1)
print(p2)
print(p1==p2 or p1 is p2)
p1.showInfo()
"""
class - object 
class : a programmer-defined type. A class definition creates a new class object
class object : an object that contains information about a programmer-defined type.
 The class object can be used to create instances of the type
 instance: An object that belongs to a class.
 embedded object: An object that is stored as an attribute of another object.
shallow copy: To copy the contents of an object, including any references to embedded
objects; implemented by the copy function in the copy module.
deep copy: To copy the contents of an object as well as any embedded objects, and any
objects embedded in them, and so on; implemented by the deepcopy function in the
copy module.
object diagram: A diagram that shows objects, their attributes, and the values of the at-
tributes.

vietnamese :
class : lop la mot khuon mau 
doi tuong : la dinh nghia cua vat the
thuc the : la mot vat cu the
XE HOI LA MOT LOP
XE TOYATA CAMRY LA MOT DOI TUONG
XE TOYATA CAMRY CUA TOI LA MOT THUC THE CUA DOI TUONG
"""