class Robot:

    raiseAmount = 100 # Declaring & Instatiating Instance variable

    def __init__(self, name, fn, weight, price): # like parameterised constructor in Java
        self.name = name
        self.fn = fn
        self.weight = weight
        self.price = price

    def introduceSelf(self): # self = this
        print("I am  {}, a {} robot".format(self.name, self.fn))

    def priceIncrease(self):
        self.price = self.price + Robot.raiseAmount

    @classmethod # like static method in java
    def createRobotFromString(cls,str):
        name,fn,weight,price = str.split('-')
        return cls(name,fn,weight,price)


    @staticmethod # just a fn, somehow related to the class, but doesn't use instance var/cls/self
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return  False
        return True



# no need of main
r1 = Robot("Tom", "household", 30, 100)
r2 = Robot("Jerry", "industrial", 20, 200)

r1.introduceSelf()
print("Price : ", r1.price)
r1.priceIncrease()
print("New Price : ", r1.price)
# accessing namespace
print(r1.__dict__)
print(Robot.__dict__)

#class methods ex
robotString = "Goofy-gardening-5-100"
r3 = Robot.createRobotFromString(robotString)
r3.introduceSelf()

#static methods
import  datetime
myDate = datetime.date(2018,4,20)
print(Robot.isWorkDay(myDate))



