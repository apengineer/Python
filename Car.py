class Car:

    raiseAmount = 100

    def __init__(self, name, make, yom,price):
        self.name = name
        self.make = make
        self.yom = yom
        self.price = price

    def introduceSelf(self):
        print("I am  a {}, make {}, year of Manufacture ".format(self.name, self.make), self.yom)

    def priceIncrease(self):
        self.price = self.price + self.raiseAmount

        #fall back method for dunder str. If only --repr-- implementes and not __str__, print(object) will execute __repr__
    def __repr__(self):
        return "Car('{}', '{}', {},{})".format("BMW X1 base", "BMW", 2009,100)

    # executes when print(object) given
    def __str__(self):
        return  '{} - {}'.format(self.name,self.make)

    # similar to getter. PPpty decorator. Can call this fn like an attribute
    @property
    def fullName(self):
        return '{} - {}'.format(self.name, self.make)

    #setter
    @fullName.setter
    def fullName(self,name):
        name , make = name.split(' ')
        self.name = name
        self.make = make




class BMW(Car):
   raiseAmount = 2500

   def __init__(self, name, make, yom, price, color):
       super().__init__(name, make, yom, price)
       self.color = color



#print(help(BMW))



c1 = BMW("BMW X1 derived", "BMW", 2009, 100,"red")
c1.introduceSelf()
c1.priceIncrease()
print(c1.price)
print(c1.color)



c1 = Car("BMW X1 base", "BMW", 2009,100)
c1.introduceSelf()
c1.priceIncrease()
print(c1.price)


c1.fullName = 'Test Ride'
print(c1.fullName)

c1.yom = 2010
print(c1.yom)

