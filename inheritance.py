##
####
####
####class A:
####
####    a = 10
####    b = 20
####
####
####class B(A):
####
####    c = 30
####
####    def add(self):
####        print(self.a+self.b+self.c)
####
####
####obj = B()
####
####obj.add()
##
##
####class A:
####    a = 10
####
####    b = 20
####
####    def show(self):
####        print(self.a+self.b)
####
####class B(A):
####
####    def display(self):
####        print("welcome")
####
####
####obj = B()
####obj.show()
####obj.display()
##
####
####class A:
####
####    def __init__(self,v1,v2):
####        self.a=v1
####        self.b=v2
####
####
####class B(A):
####
####    def __init__(self,v1,v2,v3):
####        super().__init__(v1,v2)
####        self.c=v3
####
####
####    def add(self):
####
####        print(self.a+self.b+self.c)
####
####
####
####obj = B(10,20,30)
####print(obj.a)
####
####print(obj.b)
####
####print(obj.c)
##
##
##
##
##
##class A:
##
##    def __init__(self,v1,v2):
##        self.a = v1
##        self.b = v2
##
##
##    def add(self):
##        print(self.a+self.b)
##
##    def sub(self):
##        print(self.a-self.b)
##
##
##class B(A):
##
##    def __init__(self,v1,v2,v3,v4):
##        super().__init__(v1,v2)
##
##        self.c=v3
##        self.d=v4
##
##
##
##    def square(self):
##        print(self.a**2)
##
##    def cube(self):
##        print(self.b**3)
##
##    def mul(self):
##
##        print(self.c*self.d)
##
##
##obj = B(10,20,30,40)
##
##obj.add()
##obj.sub()
##obj.square()
##obj.cube()
##obj.mul()






##class animal:
##
##    name = "Dog"
##
##    age = "20"
##
##class dog(animal):
##
##    breed = "english"
##
##    def show(self):
##        print(self.name)
##        print(self.age)
##        print(self.breed)
##
##
##
##a = dog()
##
##a.show()



##
##class shape:
##    def __init__(self,v1,v2):
##        self.a=v1
##        self.b = v2
##        
##
##
##class rectriangle(shape):
##
##    def area1(self,v1,v2):
##        super().__init__(v1,v2)
##
##        print(self.a*self.b)
##
##
##        
##b = rectriangle(10,20)
##b.area1(10,20)


##class person:
##
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##
##class emp(person):
##
####    salary = "100k"
##
##    def __init__(self,name,age,salary):
##        super().__init__(name,age)
##        self.salary=salary
##
##    def show(self):
##        print(self.name)
##        print(self.age)
##        print(self.salary)
##
##
##b = emp("roshan","39",1000)
##
##b.show()



class vehicle:
    name= "roshan"

    def details(self):
        print(self.name)
        


class car(vehicle):
    def 

    

b = car()

b.drive("roshan",1000)














































































#
