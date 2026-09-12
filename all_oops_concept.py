

##class A:
##
##    def show(self):
##        print("class a")
##
##a = A()
##a.show()
##
##class A:
##
##    a = 20
##
##class B(A):
##
##    def show(self):
##        print(self.a)
##
##a = B()
##a.show()
##class A:
##
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##
##class B(A):
##
##    def __init__(self,name,age,address):
##        super().__init__(name,age)
##        self.address = address
##
##    def display(self):
##
##        print(f"the name is a:-{self.name} the age is a:-{self.age} the address is a:-{self.address}")
##
##a = B("roshna",32,"ksaba peth")
##a.display()
##        


##class A:
##    a =20
##
##class B(A):
##
##    b = 30
##
##class C(B):
##
##    c = 40
##
##class E(C):
##
##    def show(self):
##        print(self.a+self.b+self.c)
##
##s = E()
##s.show()

##class A:
##
##    a = 20
##
##class B(A):
##
##    def show(self):
##
##        print(self.a**2)
##
##
##class C(A):
##
##    def show1(self):
##        print(self.a)
##
##c = C()
##c.show1()
##
##e = B()
##e.show()

##
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
##    def show(self):
##        print(self.a+self.b)
##
##c = C()
##c.show()
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
##class E(B,C):
##
##    def show(self):
##
##        print(self.a+self.b+self.c)
##
##e = E()
##e.show()

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
##    def show(self):
##        pass
##
##class B(A):
##
##    def show(self):
##        print("class A abstarctmethod")
##
##    def show1(self):
##        print("class A abstractmethod 1")
##
##a = B()
##
##a.show()
##a.show1()


##class A:
##
##    a = 20
##    _b =30
##    __c = 40
##
##    def show1(self):
##        print(self.a+self._b+self.__c)
##
##    def _show2(self):
##        print(self.__c)
##
##    def __show3(self):
##        print(self._b)
##
##
##    def getter(self):
##        self.__show3()
##
##c = A()
##c.show1()
##c._show2()
####A.__show3()
##c.getter()

##

##from multipledispatch import dispatch
##

##class A:
##

##    @dispatch(int)
##    def show(self,a):
##        print(a)
##

##    @dispatch(int,int)
##    def show(self,a,b):
##        print(a+b)
##
##    @dispatch(int,int,int)

##def show(self,a,b,c):
##        print(a+b+c)
##

##a = A()
##a.show(10)

##a.show(20,30)
##a.show(10,20,30)



##
##class A:

##    def show(self):
##        print("hello")

##class B(A):


##    def show(self):
##        print("not hello")


##c = B()
##c.show()



##class A:

##    def show(self):
##        print("hello boys")

##class B(A):

##    def show(self):
##        print("hellow")

##c = A()
##c.show()
  
##d = B()
##d.show()






##for i in range(0,5,1):
##    print(" "*(5-i),"*"*((2*i)-1))
##
##
##
##for i in range(4,0,-1):
##    print(" "*(6-i),"*"*((2*i)-3))

##for i in range(5,0,-1):
##    print(" "*i,"*"*(5-i))
##
##
##for i in range(0,5,1):
##    for j in range(0,5,1):
##        print("*"*j)
##
##    print()





























