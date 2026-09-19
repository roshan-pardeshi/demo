

##def A():
##
##    print("function A")
##
##    def B():
##        print("funcation B")
##
##    return B
##
##a = A()
##a()


##class A:
##
##    def A1(self):
##        print("hello class A function A1")
##
##a = A()
##a.A1()

##class A:
##
##
##    a = 20
##    b = 40
##    def static():
##        print("class A static function ",A.a+A.b)
##
##    def non_static(self):
##        print("class A non static funcation",self.a+self.b)
##
##a = A()
##a.a=20
##a.b=30
##a.non_static()
##
##
##A.static()


##class  Student:
##
##    def __init__(self,name):
##        self.a = name
##
##    def display(self):
##        print("name :-",self.a)
##
##
##
##a = Student("roshan")
##a.display()


##class A:
##
##    def __init__(self,roll_no,name,address,cgpa):
##
##        self.roll_no = roll_no
##        self.name = name
##        self.address = address
##        self.cgpa = cgpa
##
##
##    def __str__(self):
##
##        return f"roll_no:-{self.roll_no} the name:-{self.name} the address:-{self.address} the cgpa:-{self.cgpa}"
##
##
##
##
##n = int(input("enter the number of student you try to add in this record"))
##
##li=[]
##
##for i in range(n):
##    a = A(int(input("enter the roll_no")),input("enter the name"),input("enter the address"),int(input("enter cgpa")))
##    li.append(a)
##
##
##for i in li:
##    print(i)


##
##class A:
##
##    a = 20
##
##class B(A):
##
##    b = 20
##
##    def display(self):
##        print(self.a+self.b)
##
##a = B()
##a.display()



##class A:
##
##    a = 20
##
##class B(A):
##
##    b = 30
##
##class C(B):
##
##    c = 40
##
##    def display(self):
##        print(self.a+self.b+self.c)
##
##
##a = C()
##a.display()




##class A:
##
##    a = 20
##
##class B:
##
##    b = 30
##
##class C(A,B):
##
##    c = 40
##
##    def display(self):
##        print(self.a+self.b+self.c)
##
##a = C()
##a.display()



##
##class A:
##
##    a = 20
##
##class B(A):
##
##    def show(self):
##        print("Class B call",self.a)
##
##
##class C(A):
##
##    def show(self):
##        print("class C call:-",self.a)
##
##
##a = B()
##
##a.show()
##
##b = C()
####b.show()
##
##
##class A:
##
##    a = 20
##    def show(self):
##        print("class A call")
##
##class B(A):
##
##    b = 30
##    def show1(self):
##        print("class B call")
##
##class C(A):
##
##    c = 40
##
##    def show2(self):
##        print("class c call")
##
##class main(B,C):
##
##    def display(self):
##        print(self.a+self.b+self.c)
##
##a = main()
##a.display()
##a.show2()
##a.show1()
##a.show()
##
##
##
##class NegativeError(Exception):
##    pass
##
##
##try:
##
##    a = int(input("enter the positive value"))
##
##    if a<0:
##        raise NegativeError
##
##
##except NegativeError:
##    print("negative error occurs")
##
##else:
##    print(a)


##class EvenNumberError(Exception):
##    pass
##
##try:
##
##    a = int(input("enter the number"))
##
##    if a %2==0:
##        raise EvenNumberError
##
##
##except EvenNumberError:
##
##    print("even number error are occurs")
##
##else:
##
##    print(a)
##
##
##class A:
##
####    _a = 10
##
##    __b1 = 31
####
####    c = 40
##
##    def setter(self,n):
##            self.__b1=n
##
##    def show(self):
##        print("protected variable",self.a)
##        print("private variable ",self._b)
##        print("local variable",self.__b1)
##
##
##        
##
##    
##
##a=A()
##a.a=20
##a._b=40
##a.setter(30)
##a.show()



##class A:
##
##    def show(self):
##        print("local method")
##
##    def _show1(self):
##
##        print("protected method")
##        self.__show2()
##
##
##    def __show2(self):
##        print("private method")
##
##
##qa = A()
##qa.show()
##qa._show1()

##
##from abc import ABC,abstractmethod
##
##class A(ABC):
##
##    @abstractmethod
##    def show(self):
##        pass
##
##    @abstractmethod
##    def show2(self):
##        pass
##
##class B(A):
##
##    def show(self):
##        print("is a first abstractclass")
##
##    def show2(self):
##        print("is a second abstractclass")
##
##a = B()
##a.show()
##a.show2()



##from multipledispatch import dispatch

##class A:
##
##    @dispatch(int,int)
##    def show(self,a,b):
##        print("It is show method addition of two numbers:-",a+b)
##
##    @dispatch(int,int,int)
##    def show(self,a,b,c):
##        print("it is show method 2 addition of three numbers:-",a+b+c)
##
##
##a = A()
##a.show(10,20)
##a.show(30,40,40)
##
##a = 20
##
##b = "ro"
##
##print(a+b)


##st = "RoshanVijayPardeshi"
##
##li=[]
##for i in range(65,90,1):
##    if chr(i) in st:
##        li.append(chr(i))
##        
##print(li)


##class A:
##
##    def show(self):
##        print("hello class A method show1")
##
##    def show2(self):
##        print("class A method show2")
##
##class B(A):
##    pass
##
####    def show(self,a):
####        print("cLass B method show",a)
####
####    def show2(self):
####        print("class b method show`2")
##
##a = B()
####a.show(20)
##a.show2()
##a.show()
##a.show2()



##
##num = 145
##
##total = 0
##
##for i in range(1,num):
##    if num%i==0:
##        total+=i
##
##if total==num:
##    print("perfact number")
##else:
##    print("not perfect number")
##

##palindrome number

##
##num = 222
##
##
##no = num
##
##rev = 0
##
##while no>0:
##    a = no%10
##    rev = rev * 10 + a
##    no  = no // 10
##
##
##if rev == num:
##    print("palindrome number")
##else:
##    print("not a palindrome number")
##


##amstrong number
##
##
##num = 15
##
##b = len(str(num))
##
##no = num
##
##amt = 0
##
##for i in range(1,num+1):
##    a = no %10
##    amt = amt + a**b
##    no = no // 10
##
##if amt == num:
##    print("amstrong number")
##else:
##    print("not a amstrong number")
##    
##
##


##
##def factorial(n):
##
##    num = n
##
##    fact = 1
##
##    for i in range(1,num+1,1):
##        fact *=i
##
##    return fact
##
##
##num = 145
##sum1=0
##for i in str(num):
##    sum1+=factorial(int(i))
##
##if num==sum1:
##    print("strong number")
##else:
##    print("not strong number")


li = [2,4,5,6,7,8,1]

li1 = []

target = 8

for i in range(0,len(li),1):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==target:
            li1.append((li[i],li[j]))


print(li1)


                       
    

































