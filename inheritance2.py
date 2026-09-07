
##
##class A:
##
##    def add(self):
##        print("hellow")
##
##class B(A):
##
##    def sub(self):
##        print("hii")
##
##a = B()
##a.add()
##a.sub()

    
        
##class A:
##
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##
##class B(A):
##
##    def __init__(self,name,age,salary):
##        super().__init__(name,age)
##        self.salary = salary
##
##
##    def show(self):
##        print(self.name)
##        print(self.age)
##        print(self.salary)
##
##
##a = B("roshan",29,1000)
##
##a.show()

##
##
##class Animal:
##    name = "coco"
##    age = 21
##
##class Dog(Animal):
##    breed = "English"
##    
##    def show(self):
##        print(self.name)
##        print(self.age)
##        print(self.breed)
##
##
##a = Dog()
##a.show()

##
##class shape:
##
##    l = 100
##    w = 200
##
##    def area(self):
##        print("length of the rectriangle")
##        
##
##
##
##class rectriangle(shape):
##
##    def area_of(self,l,w):
##        print(self.l*self.w)
##
##
##a = rectriangle()
##a.area_of(10,20)


class A:

    def __init__(self,name,age):

        self.name = name
        self.age = age



##class B(A):
##
####    salary = "100k"
##
##
##    def __init__(self,name,age,salary):
##
##        super().__init__(name,age)
##
##        self.salary = salary
##
##
##    def person_details(self):
##        print(self.name)
##        print(self.age)
##        print(self.salary)
##
##li = []
##
##n = int(input("enter how many student you add:--"))
##for i in range(n):
##    b = B(input("enter the name"),input("enter the age"),input("enter the a salary"))
##    li.append(b)
##
##
##for i in li:
##
##    b.person_details()

##
##class vehicle:
##
##    def start(self):
##        print("hello")
##
##class car(vehicle):
##
##    def drive(self):
##        print("buy the car")
##
##b = car()
##
##b.start()
##
##b.drive()
##    



##class laptop:
##
##    
##    def __init__(self,brand,price):
##
##        self.brand = brand
##        self.price = price
##
##class gaming_laptop(laptop):
##
##     
##    def __init__(self,brand,price,grapihics_card):
##
##        super().__init__(brand,price)
##
##        self.grapihics_card =grapihics_card
##
##
##    def show(self):
##        print("brand name:-",self.brand,"price:-",self.price,"grapihics_card",self.grapihics_card)
##
##
##a = gaming_laptop("hp","10000k","4GB")
##
##a.show()



##class Book:
##
##    title = "build don't tolk"
##    author = "raj shamani"
##
##class Ebook(Book):
##
##    def download(self):
##        print(self.file_size)
##
##
##b = Ebook()
##
##print(b.title)
##print(b.author)
##b.file_size = "4 gb"
##b.download()
##
##
##class Appliance:
##
##    brand = "hp"
##    wattage = "fast speed"
##
##
##class Fan(Appliance):
##
##    speed = "very fast"
##
##    def details(self):
##        super().brand
##        super().wattage
##        
##        print(self.brand)
##
##        print(self.wattage)
##        
##        print(self.speed)

##a = Fan()
##
##a.details()


##class Shape:
##
##    def area(self):
##        print("hellow")
##
##
##class Rectriangle(Shape):
##
##
##    def show(self):
##        super().area
##        self.area()
##
##a = Rectriangle()
##
##a.show()
        



##class fruit:
##    color = ""
##    
##
##class apple(fruit):
##
##    color="red"
##
##
##
##a = apple()
##
##print(a.color)

##try:
##    a = int(input("enter the number"))
##    b = int(input("enter the number 2:"))
##
##    c = a/b
##
##except ZeroDivisionError:
##    print("is and zero division error")
##
##else:
##    print(a)
##    print(b)
##    print(c)



##try:
##    a = int(input("enter the number"))
##
##except ValueError:
##    print("value error")
##
##else:
##    print(a)


##
##try :
##    li = [1,2,3,4,5]
##
##    print(li[2])
##
##except IndexError:
##    print("is and Index Error")
##
##else:
##    print(li)


##t3ry:
##
##    a = int(input("enter the a number"))
##    b = int(input("enter the a number 2:"))
##
##    c = a/b
##
##except ValueError,ZeroDivisionError:
##    print("both error are occurs")
##
##else:
##    print(c)
##    print(a)
##    print(c)


##try:
##    fact = 1
##
##    num =int(input("enter the number"))
##
##    for i in range(1,num+1,1):
##        fact*=i
##
##    print(fact)
##
##except ValueError:
##    print("valueError")
##
##else:
##    print("is and not error",fact)


##
##try :
##
##    di = {1:"roshan",2:"sonu",3:"monu",4:"krishna"}
##
##    a = int(input("enter the roll number"))
##
##    print(di[a])
##
##except Exception as e:
##    print("is and error",e)
##
##else:
##    print(di)


##try:
##
##    st = "roshan"
##
##    st.append("roshan")
##
##except AttributeError:
##    print("is and error")
##
##else:
##    print(st)
##
##try:
##    print(c)
##
##except NameError:
##    print("is not defind")
##
##else:
##    print("sonu")


##try:
##    a = int(input("enter the number"))
##    b = int(input("enter the number1"))
##
##    c = a/b
##    
##except ZeroDivisionError:
##    print("is and error")
##
##else:
##    print(a)
##    print(b)
##    print(c)
##
##finally:
##    print("it always run")


##try:
##
##    a = int(input("enter the a number"))
##    b = int(input("enter the a number 2"))
##
##    c = a/b
####    print(d)
##
##except ValueError,ZeroDivisionError:
##    print("is and value and zero division error occurs")
##
##except Exception as e:
##    print("other error occurs",e)
##
##else:
##    print(c)

##
##
##try:
##    a = int(input("enter the number"))
##
##    c = 100/a
##
##except ValueError,ZeroDivisionError:
##    print("is an both errors occurs")
##
##else:
##    print(c)

##
##
##try:
##    st = "roshan"
##
##    li = [1,2,3,4,5,56,6]
##
##    st.append(li)
##
##except Exception as a:
##    print("is an error",a)
##
##else:
##    print(st)
##    print(li)

##
##try:
##    a = int(input("enter the a number"))
##
##    b = int(input("enter the a number"))
##
##
##    print(a+b)
##    print(a/b)
##    print(a*b)
##
##
##except ValueError,ZeroDivisionError:
##    print("is and error")
##    
##          
##else:
##    print("currect")



##class NegativeError(Exception):
##    pass
##
##try:
##    a = int(input("enter the a number +ve :--"))
##
##    if a<0:
##        raise NegativeError
##
##except NegativeError:
##    print("is and -ve error")
##
##else:
####    print(a)
##
##
##d1 = {}
##
##n = 5
##
##for i in range(n):
##    a = int(input("enter the number"))
##    d1[i]=a**2
##
##
##print(d1[2])

##class SmallStringError(Exception):
##    pass
##
##try:
##
##    st = "rosn"
##
##    if len(st)<5:
##        raise SmallStringError
##
##except SmallStringError:
##    print("is an small string error")
##
##else:
##    print(st)
        


##class EvenNumberError(Exception):
##    pass
##
##try:
##    a = int(input("enter the a number:--"))
##
##    if a%2==0:
##        raise EvenNumberError
##
##except EvenNumberError:
##    print("user input is a Even number")
##
##else:
##    print(a)

##
##li = [1,2,-3,4,-3,-5,-6]
##
##
##res = list(map(lambda x:x*(-1)  if x<0 else x,li))
##
##print(res)
##
##
##class AgeValidationError(Exception):
##    pass
##
##try:
##    age = int(input("enter your age:--"))
##
##    if age<18 or age>100:
##        raise AgeValidationError
##
##except AgeValidationError:
##    print("age validation error are occurs")
##
##else:
##    print("your are age is  valid:--",age)
##
##
##class PasswordValidationError(Exception):
##    pass
##
##try:
##    pass_word = input("enter the a password")
##
##    if pass_word.isalnum() and  len(pass_word)>8 and pass_word.upper():
##        pass
##    else:
##        raise PasswordValidationError
##
##except PasswordValidationError as n:
##    print("is an password validation error",n)
##
##else:
##    print("your password is a:-",pass_word)


class InvalidRollNumberError(Exception):
    pass

##
##try:
##    d1 = {1:"roshan",2:"sonu",3:"monu",4:"golu"}
##
##    d = d1.keys()
##
##    n = int(input("enter the rollnumber"))
##
##    if n not in d:
##        raise InvalidRollNumberError
##
##except InvalidRollNumberError:
##    print("is and Error")
##
##
##else:
##    print(d1)



##class OutOfStockError(Exception):
##    pass
##
##try:
##    onion = 100
##
##  
##
##    
##    while True:
##        user = int(input("enter the product quantity"))
##
##        if onion>user:
##            onion-=user
##        else:
##            raise OutOfStockError
##        
##
##except OutOfStockError:
##    print("product out of the stock")
##
##else:
##    print(onion)



##class ZeroInputError(Exception):
##    pass
##
##
##try:
##    a = int(input("enter the number"))
##
##    if a==0:raise ZeroInputError
##
##except ZeroInputError:
##    print("zero input inserted by the a user")
##
####else:print(a)
##
##
##class DivisionByNegativeError(Exception):
##    pass
##
##try:
##    a = int(input("enter the a number"))
##    b = int(input("enter the a number 2"))
##
##    if a<0 or b<0:
##        raise DivisionByNegativeError
##
##except DivisionByNegativeError:
##    print("is and a negative number")
##
##else:
##    print("a",a,"b",b)

##    
##class ShortNumberError(Exception):
##    pass
##
##try:
##
##    a = int(input("enter the a number"))
##
##    if len(str(a))<3:
##        raise ShortNumberError
##
##except ShortNumberError:
##    print("is and a error occurse during excution")
##
##else:
##    print(a)

##
##class OddNumberError(Exception):
##    pass
##
##
##try:
##    a = int(input("enter the number"))
##
##    if a%2!=0:
##        raise OddNumberError
##
##except OddNumberError:
##    print("odd number errors occurs")
##
##else:
##    print("a",a)

##class A:
##
##    def __init__(self,name,age,address):
##        self.name = name
##        self.age = age
##        self.address = address
##
##    def __str__(self):
##
##        return f"Name :-{self.name} Age :-{self.age} Address:-{self.address}"
##
##
##n = int(input("enter the number how many student you try to add in give program"))
##li=[]
##for i in range(n):
##    a = A(input("name :-"),int(input("enter the a age:-")),input("address is a:-"))
##    li.append(a)
##
##
##for i in li:
##    print(i)


##li = [1,2,3,4,1,2]
##res = []
##for i in li:
##    if li.count(i)>1 and i not in res:
##        res.append(i)
##
##
##
##print(res[1])


class MarksOutOfRange(Exception):
    pass


try:
    marks = int(input("enter the marks:-"))

    if marks<0 or marks>100:
        raise MarksOutOfRange

except MarksOutOfRange:
    print("marks out of the range")

else:
    print("not out of the range")
    






















    

















































































































































































































