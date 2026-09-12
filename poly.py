

##from multipledispatch import dispatch
##
##
##class A:
##    @dispatch(int,int)
##    def add(self,a,b):
##        print("the addition is :-",a+b)
##
##    @dispatch(int,int,int)
##    def add(self,a,b,c):
##        print("three number addition",a+b+c)
##
##    @dispatch(int)
##    def add(self,a):
##        print("square is a",a**2)
##
##obj = A()
##obj.add(10,20)
##obj.add(10,20,30)
##obj.add(20)






##class A:
##
##    def operation(self):
##        print("class A")
##
##class B(A):
##
##    def operation(self,a):
##        print("square is a:-",a**2)
##
##class C(B):
##
##    def operation(self,a):
##        print("cube is a:-",a**3)
##
##class D(C):
##
##    def operation(self,a):
##
##        for i in range(1,11,1):
##            print(a*i)
##
##obj = A()
##obj.operation()
##
##obj1 = B()
##obj1.operation(20)
##
##obj2 = C()
##obj2.operation(30)
##
##obj3 = D()
##obj3.operation(30)


##
##class Calculator:
##
##    def operation(self):
##        print("calculator")
##
##class add(Calculator):
##
##
##    def operation(self,a,b):
##        print(a+b)
##
##class sub(add):
##
##    def operation(self,a,b):
##        print(a-b)
##
##
##class square(sub):
##
##    def operation(self,a):
##        print("square is a:-",a**2)
##
##
##obj = Calculator()
##obj.operation()
##
##
##obj1 = add()
##obj1.operation(20,30)
##
##obj2 = sub()
##obj2.operation(30,40)
##
##obj3 = square()
##obj3.operation(5)


##from multipledispatch import dispatch
##
##class calculator:
##
##    @dispatch(int)
##    def show(self,a):
##        print(a**2)
##
##    @dispatch(str)
##    def show(self,a):
##        print("the product is a",a)
##
##    @dispatch(int,int,int)
##    def show(self,a,b,c):
##        print("multiplication is a",a*b*c)
##
##
##a = calculator()
##a.show(2)
##a.show("roshan")
##a.show(20,30,40)
##        



##from multipledispatch import dispatch
##
##class Printer:
##
##    @dispatch(str)
##    def print_data(self,a):
##        print(a.upper())
##
##    @dispatch(list)
##    def print_data(self,a):
##        for i in a:
##            print(i)
##
##    @dispatch(dict)
##    def print_data(self,a):
##        print(a)
##
##
##d = Printer()
##d.print_data("roshan")
##
##li = [1,2,3,4,5]
##
##d.print_data(li)
##
##e = {1:"roshan",2:"sonu"}
####
####
####d.print_data(e)
##        
##
##from multipledispatch import dispatch
##
##
##class overload:
##
##    @dispatch(int)
##    def show(self,a):
##        print(f"square is a:-{a**2}")
##
##    @dispatch(str)
##    def show(self,a):
##        print(f"uppercase :-{a.upper()}")
##
##    @dispatch(list)
##
##    def show(self,a):
##        count = 0
##
##        for i in a:
##            count+=1
##
##        print("total list element is a:-",count)
##
##c = overload()
##
##c.show(20)
##c.show("string")
##li = [1,2,3,4,5,6]
##c.show(li)


##from multipledispatch import dispatch
##
##class bill:
##
##    @dispatch(int,str,int)
##    def generate_bill(self,a,b,c):
##        if b=="5 star" and a==5:
##            print(f"the product name is a:-{a} and quantity is a:-{b} and price is a :-{c}")
##
##    @dispatch(int)
##    def generate_bill(self,a):
##        print("your total bill is a :-:",a)
##
##a= bill()
##
##a.generate_bill(5,"5 star",100)
##
##a.generate_bill(10000)

##        
##from multipledispatch import dispatch
##
##class parameter:
##
##    @dispatch(str)
##    def display(self,name):
##        print(f"the name is a:-{name}")
##
##    @dispatch(str,int)
##    def display(self,name,marks):
##        print(f"student name is a:{name} the student marks is a:{marks}")
##
##    @dispatch(str,int,str)
##    def display(self,name,marks,grade):
##        print(f"the name {name} the marks:{marks} the grade:-{grade}")
##
##
##a = parameter()
##
##a.display("roshan")
##
##a.display("roshan",30)
##
##a.display("roshan",30,"C")
    

##class A:
##
##    def withdraw(self):
##        print("class A witdraw")
##
##class S(A):
##
##    def withdraw(self,a):
##        print("Class S withdraw",a)
##
##class C(S):
##
##    def withdraw(self,a):
##        print("Class C withdraw",a)
##
##a = A()
##a.withdraw()
##
##b = S()
##b.withdraw(10)
##
##c = C()
##c.withdraw(20)
        



##class Employee:
##
##    def calculate_salary(self):
##        print("the a employee class")
##
##
##class permanentEmp(Employee):
##
##    def calculate_salary(self,salary,bonus):
##        print(salary+bonus)
##
##
##class ContractEmp(Employee):
##
##    def calculate_salary(self,salary,incentive):
##        print(salary+incentive)
##
##
##a = Employee()
##a.calculate_salary()
##
##b = permanentEmp()
##b.calculate_salary(1000,2)
##
####c = ContractEmp()
####c.calculate_salary(2000,20)
##
##
##class Transport:
##
##    def fare(self):
##        print("the a fare is in Transport class")
##
##class Bus(Transport):
##
##    def fare(self):
##
##        print("bus ticket is very low")
##
##class Train(Transport):
##
##    def fare(self):
##        print("the train ticket is very very low")
##
##class Taxi(Transport):
##
##    def fare(self):
##
##        print("the  a taxi ticket is very expensive")
##
##
##a = Transport()
##a.fare()
##
##b = Bus()
##b.fare()
##
##c = Train()
##c.fare()
##
##d = Taxi()
##d.fare()



##class Animal:
##
##    name = "coco"
##    sound = "bark"
##
##class Dog(Animal):
##
##
##    def display(self,breed):
##        print(f"dog name:-{self.name} the dog sound:-{self.sound} the breed of the Dog is :-{breed}")
##
##
##
##d = Dog()
##d.display("engilsh")


##
##
##
##class Shape:
##
##    def area(self,l,w):
##        print(l*w)
##
##
##class Rectriangle(Shape):
##
##    def display(self):
##        super().area(20,30)
##
##
##a = Rectriangle()
##a.display()
        
        
##
##class Person:
##
##
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##
##class Employee(Person):
##
##    def __init__(self,name,age,salary):
##        super().__init__(name,age)
##        self.salary = salary
##
##
##    def display(self):
##        print(f"the name :-{self.name} the age is a:-{self.age} the a salary is a:-{self.salary}")
##
##a = Employee("roshan",21,0)
##a.display()




##class Vehicle:
##
##    def start(self):
##        print("the class is start very fast")
##
##class Car(Vehicle):
##
##    def drive(self):
##        print("the drive is nexon")
##
##a = Car()
##a.drive()
##a.start()

##class Laptop:
##
##
##    def __init__(self,brand,price):
##        self.brand = brand
##        self.price = price
##
##
##class GamingLaptop(Laptop):
##
##    def __init__(self,brand,price,graphics_card):
##
##        super().__init__(brand,price)
##
##        self.graphics_card = graphics_card
##
##
##    def display(self):
##        print(f"the brand is:-{self.brand} the price:-{self.price} the graphices_card:-{self.graphics_card}")
##
##a = GamingLaptop("Dell",1000,"4gb")
##
##a.display()


##class Book:
##
##    title = "build don't tolk"
##    author = "Raj shamani"
##
##
##class EBook(Book):
##
##    def donwload(self,file_size):
##        print(f"the a tiltle is :{self.title} the a author is a:{self.author} the file sales is a:-{file_size}")
##
##
##
##a = EBook()
##
##a.donwload(300)

##
##class Applienace:
##
##    brand = "Amstrong"
##    wattage = "120w"
##
##class Fan(Applienace):
##
##    def show(self,speed):
##        print(f"the a brand is a:{self.brand} the wattage:{self.wattage} the speed is a:{speed}")
##
##a = Fan()
##a.show(120)



##class Shape:
##
##    def area(self):
##
##        print("is an area")
##
##class Circle(Shape):
##
##    def area1(self):
##        self.area()
##
##
##class Rectriangle(Circle):
##
##    def area2(self):
##
##        self.area()
##
##        
##a = Circle()
##a.area1()
##
##b = Rectriangle()
##b.area2()


##
##
##class Fruit:
##
##    color=""
##
##
##class Apple(Fruit):
##
##    color = "red"
##
##    print(color)
##
##a = Apple()


##
##class Student:
##
##    __name = ""
##    __age = 0
##
##    def setter(self,a,b):
##        self.__name=a
##        self.__age=b
##
##    def getter(self):
##        print(self.__name,self.__age)
##
##
##a = Student()
##a.setter("roshan",21)
##
##a.getter()



##class BankAccount:
##
##    __balance = 1000
##
##    def deposit(self,amt):
##        self.__balance+=amt
##
##    def withdraw(self,amt):
##        if self.__balance>0:
##            self.__balance-=amt
##
##    def display(self):
##        print(f"your balance is a:{self.__balance}")
##
##
##a = BankAccount()
##a.deposit(200)
##a.display()
##a.withdraw(300)
##a.display()

##
##class Employee:
##
##    _salary = 1000
##    __bonus = 10
##
##
##    def display(self):
##        print("private attribute",self.__bonus)
##        print("protected attribute",self._salary)
##
##class Manager(Employee):
##
##    def show(self):
##        print(self._salary)
##
##a = Manager()
##a.show()
##a.display()

##
##class Car:
##
##    __brand = "tata"
##    __speed = 120
##
##    
##    def setter(self):
##        if self.__speed>=120:
##            print("is getter")
##
##    def getter(self):
##        print(f"the brand is a{self.__brand} the speed is a{self.__speed}")
##            
##
##
##c = Car()
##c.setter()
##c.getter()




##class School:
##
##    def pubilc_info(self):
##        print("is and public method")
##
##    def _protected_info(self):
##        print("is and protected method")
##
##    def __private_method(self):
##        print("is and private method")
##
##    def getter(self):
##        self.__private_method()
##
##
##s = School()
##s.pubilc_info()
##
##s._protected_info()
##
##s.getter()




##class Atm:
##
##    __pin = 1234
##    _balance = 200000
##    
##
##    def set_pin(self,new_pin):
##        if new_pin==4:
##            self.__pin = new_pin
##            print("pin set successfully")
##
##
##    def validate_pin(self,a):
##        if a == self.__pin:
##            print("is an validate pin")
##
##    def __display_balance(self,a):
##        if a == self.__pin:
##            print("the total balance is a",self._balance)
##
##
##    def getter(self):
##        self.__display_balance(1234)
##
##a = Atm()
##a.set_pin(1234)
##
##a.validate_pin(1234)
##
##a.getter()
##
##

##
##from abc import ABC,abstractmethod
##
##
##class Shape(ABC):
##
##    @abstractmethod
##    def area(self):
##        pass
##
##    @abstractmethod
##    def peimeter(self):
##        pass
##
##class Rectriangle(Shape):
##
##    def area(self,l,w):
##        print(l*w)
##
##    def peimeter(self,l,w):
##        print(2*(l+w))
##
##c = Rectriangle()
##c.area(10,20)
####c.peimeter(10,20)
##
##    
##
##
##from abc import ABC,abstractmethod
##
##class vehicle(ABC):
##
##    @abstractmethod
##    def start(self):
##        pass
##
##    @abstractmethod
##    def s(self):
##        pass
##
##    
##class Car(vehicle):
##
##    def start(self):
##        print("the car is start")
##
##class Bike(vehicle):
##
##    def start(self):
##        print("the a bike is start")
##
##c = Car()
##c.start()
##
##b = Bike()
##b.start()


##
##from abc import ABC,abstractmethod
##
##
##class Employee(ABC):
##
##
##    @abstractmethod
##    def calculate_salary(self):
##        pass
##
##class Developer(Employee):
##
##    def calculate_salary(self,salary,bonus):
##        print(salary+bonus)
##
##
##class Manager(Employee):
##
##    def calculate_salary(self,salary,incentive):
##        print(salary+incentive)
##
##
##a = Developer()
##a.calculate_salary(2000,100)
##
##b = Manager()
##
##b.calculate_salary(20,3)



##from abc import ABC,abstractmethod
##
##class BankAccount(ABC):
##
##    @abstractmethod
##    def deposite(self):
##        pass
##
##    @abstractmethod
##    def withdrawl(self):
##        pass
##
##class Saving(BankAccount):
##
##    balance = 10000
##
##    def deposite(self,amt):
##        self.balance+=amt
##        print(self.balance)
##
##    def withdrawl(self,amt):
##        if self.balance >500 and self.balance-amt>500:
##            self.balance-=amt
##            print(self.balance)
##            
##a = Saving()
##
##a.deposite(100)
##
##a.withdrawl(234)



##from abc import ABC,abstractmethod
##
##
##class Payment(ABC):
##
##    @abstractmethod
##    def pay(self):
##        pass
##
##
##class CreditCard(Payment):
##
##    def pay(self,amt,dis_m):
##        print("total payment of the a credit card is a:-",amt+dis_m)
##
##class PaypalPayment(Payment):
##
##    def pay(self,amt,tax):
##
##        s = amt+(amt*tax/100)
##
##        print("total payment of the paypal is a:-",s)
##
##
##class UpiPayment(Payment):
##
##    def pay(self,amt):
##        print("uni never charge any fees to the user")
##
##
##a = CreditCard()
##a.pay(100,10)
##
##b = PaypalPayment()
##b.pay(100,25)
##
##c = UpiPayment()
##c.pay(1000)

##from abc import ABC,abstractmethod
##
##
##class Animal(ABC):
##
##    @abstractmethod
##    def sound(self):
##        pass
##
##    @abstractmethod
##    def move(self):
##        pass
##
##
##class Dog(Animal):
##
##    def sound(self):
##        print("dog sound is like a bulk bhuu bhuu")
##
##    def move(self):
##        print("dog movement is very fast")
##
##class Bird(Animal):
##
##    def sound(self):
##        print("the bird is fly on sky")
##
##    def move(self):
##        print("the bird movement is like a chirp somthings")
##
##class Fish(Animal):
##
##    def sound(self):
##        print("the fish is a run in water")
##
##    def move(self):
##        print("the fish is produces the bubbles")
##
# #a = Fish()
# #a.sound()
# #a.move()
##        
# #b = Dog()
# #b.sound()
# #b.move()
##
# #c = Bird()
# #c.sound()
# #c.move()
##    


##
##from abc import ABC,abstractmethod
##
##class Appliance(ABC):
##
##    @abstractmethod
##    def turn_on(self):
##        pass
##
##class TV(Appliance):
##
##    def turn_on(self):
##        print("the Tv is turn on if you click the button and play the song")
##
##class Washingmachine(Appliance):
##
##    def turn_on(self):
##        print("the washing mashingmachine is a on if you put the clothes")
##
##a  = TV()
##a.turn_on()
##
##b = Washingmachine()
##b.turn_on()



class emp:

    company = "abc"

    def __init(self,name):
        self.name = name

    def change_company(self):
        self.company = "XYZ"


e1 = emp("roshan")

e2 = emp("amit")

e1.change_company()

print(e1.company)
print(e2.company)

print(emp.company)











































