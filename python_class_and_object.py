##
##class Student:
##
##    name = "roshan"
##    roll_number = 12
##    course = "datascience"
##
##obj = Student()
##print(obj.name)
##print(obj.roll_number)
##print(obj.course)

##class Employee:
##
##    Employee_id = 1
##    Employee_name = "roshan"
##    Salary = 10000
##
##obj = Employee()
##print(obj.Employee_id)
##print(obj.Employee_name)
##print(obj.Salary)


##class Car:
##
##    brand = ""
##    Model=""
##    price = 0
##
##obj = Car()
##obj.brand = "tata"
##obj.model="2017"
##obj.price = 20000
##
##print(obj.brand)
##print(obj.model)
##print(obj.price)


##class Book:
##
##    Book_name = "Build Don't Tolk"
##    author = "Raj shamani"
##    Price = 1000
##
##obj = Book()
##
##print(obj.Book_name)
##print(obj.author)
##print(obj.Price)


##class Mobile():
##
##    Brand = "vivo"
##    ram = "4GB"
##    Price = 10000
##
##obj = Mobile()
##print(obj.Brand)
##print(obj.ram)
##print(obj.Price)


##class Student:
##
##    name = "roshan"
##    age= 21
##
##    def display(self):
##        print(f"name is a:-{self.name} the age is a:-{self.age}")
##
##obj = Student()
##obj.display()

##class A:
##
##    def show(self):
##        print("a")
##
##class B(A):
##
##    def show(self):
##        print("class B")
##
##
##obj = B()
##obj.show()

##
##class Teacher:
##
##    Teacher_Name = "Ravi Sir"
##    Subject = "DataScience"
##    Experience = "1 year"
##
##    def teacher_info(self):
##
##        print(self.Teacher_Name,self.Subject,self.Experience)
##
##
##
##obj = Teacher()
##obj.teacher_info()



##class A:
##
##    def Add(a,b):
##        print(a+b)
##
##A.Add(20,30)
##
##class Rectriangle:
##
##    length = 100
##    width = 200
##
##    def area(self):
##        print(self.length*self.width)
##
##obj = Rectriangle()
##
##obj.area()


##from math import pi
##class A:
##
##    def area(r):
##        print(pi*r*r)
##
##obj = A()
##A.area(20)

##
##class BankAccount:
##
##    Account_number = "123455"
##    Account_Holder_Name = "Roshan Vijay pardeshi"
##    Balance = 0
##
##    def display_balance(self):
##        print("acc_no:-",self.Account_number,"Acc_holder:-",self.Account_Holder_Name,"Balance:-",self.Balance)
##
##obj = BankAccount()
##obj.display_balance()


##class A:
##
##
##    def __init__(self,name,age,depart,salary):
##        self.name = name
##        self.age = age
##        self.depart = depart
##        self.salary = salary
##
##
##    def __str__(self):
##
##        return f"the name:{self.name} the age {self.age} the depart:{self.depart} the salary:{self.salary}"
##
##
##n = int(input("how many student you try to impliment in your record"))
##li=[]
##for i in range(n):
##    a = A(input("enter the name:-"),input("enter the a age"),input("enter the a department:-"),input("enter the salary"))
##    li.append(a)
##
##
##li1 =[]
##
##for i in range(0,len(li),1):
##    li1.append(i)
##    file = open("python.txt","w")
##    file.writelines("roshan",i)


##file = open("python.txt","r")
##
##print(file.readlines())


##
##
##class Number:
##
##    def print_number(self):
##        for i in range(1,11,1):
##            print(i)
##
##
##o = Number()
##o.print_number()

##
##class A:
##
##    def reverse_number(self):
##        for i in range(12,0,-1):
##            print(i)
##
##
##obj = A()
##obj.reverse_number()



class Even:

    def even_number(self):

        for i in range(1,21,1):
            if i%2==0:
                print(i)

obj = Even()
obj.even_number()



































