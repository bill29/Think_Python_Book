class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
    def printTime(time):
        print(str(time.hours) + ":" + \
        str(time.minutes) + ":" + \
        str(time.seconds))
    #overloading
    def __add__(self, other1):
        return 'hello this is a overloading method'
#Polymorphism
class Point:
    def __init__(self, x=0, y=0):
        self.x= x
        self.y= y
    def __add__(self, other):
        return str(self.x), str(self.y)
    def muladd(self, other1, other2):
        return (self.x*other1.x+other2.x, self.y*other1.y + other2.y)




"""
point1 = Point(1, 2)
point2 = Point(2, 3)
point3 = Point(1, 10)
print(muladd(1, 2, 3))
print(Point.muladd(point1, point2, point3))
currentTime = Time(9, 14, 30)
currentTime.printTime()
print(currentTime.__str__())
currentTime2 = Time()
currentTime2.printTime()
currentTime3 = Time(9)
currentTime3.printTime()
print(currentTime.__add__(currentTime2))
"""


