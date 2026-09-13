

##def welcome():
##    print("welcome sir")
##
##
##welcome()
##
##
##class College_Name():
##
##    print("gangamai college of engineering")
##
##College_Name()
##
##def display_info():
##
##    name = "roshan"
##    city = "pune"
##    course = "datasecience"
##
##    print(name,city,course)
##
##display_info()
##
##def table_multiplication():
##
##    for i in range(1,11,1):
##        print(5*i)
##
##table_multiplication()
##
##def pattern():
##
##    for i  in (1,6,1):
##        for j in range(1,6,1):
##            print("*"*5)
##
##
##pattern()



##def current_year():
##
##    print("2026")
##
##current_year()


##def even_number():
##
##    for i in range(1,20,1):
##        if i%2==0:
##            print(i)
##
##even_number()


##def python_topic():
##
##    print("function")
##    print("oops concept")
##    print("encapsulation")
##    print("inheritance")
##    print("ploymorpishm")
##    print("abstarction")
##
##python_topic()


##def company_name():
##    print("tcs")
##
##company_name()


##def motivation():
##
##    print("your big motivation is your father beacuse he work hard to bulid your future")
##
##motivation()


##def add(a,b):
##
##    print(a+b)
##
##
##add(10,20)
##
##
##def sub(a,b):
##    print(a-b)
##
##sub(20,10)
##
##def mul(a,b):
##
##    print(a*b)
##
##mul(10,20)
##
##
##def square(a):
##
##    print(a**2)
##
##square(20)
##
##
##def cube(a):
##
##    print(a**3)
##
##cube(3)
##
##def table(n):
##
##    for i in range(1,11,1):
##        print(n*i)
##
##table(6)
##
##def student(name,age):
##
##    print(name)
##    print(age)
##
##student("roshan",12)
##
##from math import pi
##
##def circle(r):
##
##    print(pi*r*r)
##
##circle(20)
##
##def rectriangle(l,w):
##
##    print("rectriangle",l*w)
##
##rectriangle(10,20)
##
##def percentage(total_m,obtain_m):
##
##    a = total_m/obtain_m*100
##    print("percentage",a)
##
##percentage(10,20)
##
##def largest(a,b):
##
##    if a>b:
##        print("A is largest number")
##    else:
##        print("b is largest number")
##
##largest(10,20)


class A:
    li={}


    
    def __init__(self,name,age):

        self.name = name
        
        self.age = 20


    def df(self):
        file = open("python.txt","w")
        file.writelines(self.li)
        file.close()

    def read(self):
        file = open("python.txt","r")
        print(file.read())
        file.close()

    def display(self,n):
        
##        self.li.append(self.name)
##        self.li.append(self.age)
        for i in range(0,1,1):
            self.li[self.name]=self.age
            self.df()

n = 5
li1 = []
for i in range(n):
    o = A(input("enter name"),input("enter the age"))
    li1.append(o)
    
    

for i in li1:
    o.display(i)
    o.read()
            
        


























