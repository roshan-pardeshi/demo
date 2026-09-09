
##
##class A:
##
##    a = 20
##    b = 30
##
##
##class B(A):
##
##    def show(self):
##        print(self.a)
##        print(self.b)
##
##a = B()
##a.show()
##
##class A:
##
##    a = 10
##    b = 20
##
##class B(A):
##     c = 20
##     d = 30
##
##class C(B):
##
##    def show(self):
##
##        print(self.a)
##        print(self.b)
##        print(self.c)
##        print(self.d)
##
##
##d = C()
##d.show()



##
##class A:
##
##    a = 20
##
##class B:
##
##    b = 30
##
##class C:
##
##    c = 40
##
##
##
##class D(A,B,C):
##
##    def show(self):
##
##        print(self.a+self.b+self.c)
##
##
##d = D()
##d.show()
##
##class A:
##
##    a = 20
##
##class B(A):
##
##    def show1(self):
##        print("B:- class",self.a)
##
##class C(A):
##
##    def show2(self):
##        print("C:- class",self.a)
##
##class D(A):
##
##    def show3(self):
##        print("D:- class",self.a)
##
##a1 = B()
##a1.show1()
##
##b = C()
##b.show2()
##
##c = D()
##c.show3()
    



##
##class A:
##
##    a = 20
##
##class B(A):
##
##    b = 30
##
##
##class C(A):
##
##    c = 40
##
##class D(B,C):
##
##    def show(self):
##
##        print(self.a+self.b+self.c)
##
##
##s = D()
##s.show()


##class A:
##
##    a = 20
##
##    _b = 30
##
##    __c=30
##
##
##o = A()
##print(o.a)
##
##print(o._b)
##
##print(o.__c)

##
##class A:
##
##    a = 10
##
##    _b = 20
##
##    __c=30
##
##
##    def getter(self):
##        print(self.__c)
##
##    def setter(self,v1):
##        self.__c=v1
##
##
##o = A()
##
##print(o.a)
##
##print(o._b)
##
##o.getter()
##
##o.setter(20)
##
##o.getter()

##class  A:
##
##    __name = "roshan"
##    __age = 21
##
##    def setter(self,v1,v2):
##        self.__name = v1
##        self.__age = v2
##
##
##    def getter(self):
##        print(self.__name)
##        print(self.__age)
##
##
##o = A()
##
##o.getter()
##
##o.setter("sonu",30)
##
##o.getter()
##
##
##
##
##class BankAccount:
##
##    __balance = 10000
##
##    amount=2000
##
##    withdraws = 200
##
##    def deposit(self):
##        s = self.__balance+self.amount
##        print(s)
##
##
##    def withdraw(self):
##        if self.__balance>0:
##            d = self.__balance-self.withdraws
##            print(d)
##
##    def show_balance(self):
##        print(self.__balance)
##
##
##o = BankAccount()
##
##
##o.deposit()
##
##o.withdraw()
##
##o.show_balance()
##
####
##class Employee:
##
##    _salary = 2000
##    __bonus = "20%"
##
##    def display(self):
##        print(self._salary)
##        print(self.__bonus)
##
##class manager(Employee):
##
##    def show(self):
##        print(self._salary)
##
##
##a = manager()
##
##a.show()
##a.display()
##
##
##
####class Car:
####
####    __brand = "Tata"
####
####    __speed = "220"


    
##class A:
##
##    __name = "roshan"
##
##    __age = 21
##
##    def setter(self,v1,v2):
##
##        self.__name = v1
##        self.__age = v2
##
##
##    def getter(self):
##        print(self.__name)
##        print(self.__age)
##
##
##a = A()
##
##a.getter()
##
##a.setter("sonu...",22)
##
####a.getter()
##
##
##
##
##class BankAccount:
##    __balance = 10000
##
##    def deposit(self):
##        s = self.__balance+self.amount
##        print(s)
##
##    def withdraw(self):
##        if self.__balance>0:
##            d = self.__balance-self.amount
##            print("total balance",d)
##
##    def show(self):
##        print(self.__balance)
##
##
##a = BankAccount()
##a.amount = 2000
##a.deposit()
##a.amount = 300
##a.withdraw()
##a.show()





##
##class Employee:
##    _salary = 10000
##    __bonus = "20%"
##
##
##    def display(self):
##
##        print(self._salary)
##        print(self.__bonus)
##
##
##class Manager(Employee):
##
##    def details(self):
##        print(self._salary)
##
##
##a = Manager()
##a.display()
##a.details()


##class Car:
##    __brand = "TATA"
##    __speed = 120
##
##    def setter(self,v1,v2):
##        self.__brand = v1
##        self.__speed = v2
##
##    def getter(self):
##        print(self.__brand)
##        print(self.__speed)
##
##
##a = Car()
##
##a.setter("maruti swfit",300)
##
##a.getter()


##class A:
##
##    def public(self):
##        print("public class")
##
##    def __private(self):
##        print("private method")
##
##    def _protected(self):
##        self.__private()
##        print("protected method")
##
##a = A()
##
##a.public()
##a._protected()

##
##class A:
##
##    __pin = int(input("enter the pin only four letter are allowed"))
##
##    __balance = "100k"
##
##    def set_pin(self):
##        if len(str(self.__pin))==4:
##            print("your pin :--",self.__pin)
##
##    def __method_display_balance(self):
##        if self.__pin==1234:
##            print(self.__balance)
##
##    def validate(self):
##        self.__method_display_balance()
##        print("not validate")
##
##
##a = A()
##
##a.set_pin()
##
##a.validate()





##class A:
##
##    def area(self):
##        print("is an a area method of class A")
##
##
##class B(A):
##
##    def area1(self):
##        super().area()
##
##    def area3(self):
##        print(self.area())
##
##a = B()
##
##a.area1()
##a.area3()



##class A:
##
##    a = 20
##
##class B(A):
##
##    def area(self):
##        print(self.a)
##
##a = B()
##a.area()

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
##class D(C):
##
##    def show(self):
##
##        print(self.a+self.b+self.c)
##
##a = D()
##
##a.show()
##
##
##class A:
##
##    a = 20
##
##
##class B:
##
##    b  = 30
##
##
##class C(A,B):
##
##    def show(self):
##
##        print(self.a+self.b)
##
##
##c = C()
##
##c.show()


##class A:
##
##    a = 20
##    b = 20
##
##    
##class B(A):
##
##    def show(self):
##        print(self.a)
##
##class C(A):
##    
##    def show1(self):
##        print(self.a+self.b)
##
##a = B()
##
##a.show()
##
##b = C()
##
##b.show1()
##
##

##
##class A:
##
##    a = 20
##
##class B(A):
##
##    b = 20
##
##class C(A):
##
##    c = 30
##
##
##
##class D(B,C):
##
##    def show(self):
##
##        print(self.a+self.b+self.c)
##
##a = D()
##
##a.show()




##
##li= [3,1,3,4,4,5,4]
##max1 = 0
##for i in li:
##
##    if li.count(i)>1:
##        max1 = i
##
##
##print(max1)


##li  = [3,2,4]
##li1 = []
##
##for i in range(1,len(li),1):
##    if li[i]%2==0:
##        li1.append(i)
##
##print(li1)


##li = [2,7,11,15]
##
##li1 = []
##
##for i in li:
##    print(i[2]+2)
##
##print(li1)





##li = [2,7,11,15]
##
##li1=[]
##for i in range(0,len(li),1):
##    for j in range(i+1,len(li)):
##        if li[i]+li[j]==9:
##            li1.append(i)
##            li1.append(j)
##
##
##print(li1)





##
##num = 12
##
##
##
##num = str(num)
##
##if num==num[::-1]:
##    print("palindrome number")
##
##else:
##    print("not  palndrome")
##

##def factorial(n):
##
##    num = n
##
##    fact = 1
##
##    for i in range(1,num+1,1):
##        fact*=i
##
##    return fact
##
##
##num = 14
##sum1 = 0
##for i in str(num):
##    sum1+=factorial(int(i))
##
##
##
##if sum1==num:
##    print("strong number")
##

##num = 28
##cube=0
##for i in range(num):
##    a = num%2
##    cube = cube+a
##    num=num//2
##
##    
##print(cube)
##print(a)














































































































































