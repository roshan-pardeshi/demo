##
##
####class Student:
####
####    name = "roshan"
####    age  = 21
####    address = "kusumba"
####
####    def display(self):
####        print(f"the student name:{self.name}the a age is a:{self.age} the address is a:-{self.address}")
####
####a = Student()
####a.display()
####
####b = Student()
####b.display()
######              
####
####class Employee:
####
####    name = "Roshan"
####    salary = 21000
####
####    def display(self):
####        print(f"the Name of employee is a:{self.name} the salary of employee:{self.salary}")
####
####
####class Developer(Employee):
####
####    language = "English"
####
####    def display_developer_details(self):
####
####        print(f"Name:{self.name} the a salary:{self.salary} the language:{self.language}")
####
####a = Developer()
####a.display()##
####a.display_developer_details()
##
##
####
####
####class Animal:
####
####    def sound(self):
####        print("the animal sound")
####
####class Dog(Animal):
####
####    def sound(self):
####        print("dog bark")
####
####
####a = Dog()
####
####a.sound()
##
##
##
####class BankAccount:
####
####    account_number = 123456
####
####    __balance = 100000
####
####
####    def deposit(self,amount):
####
####        self.__balance+=amount
####
####
####    def withdraw(self,amount):
####        if self.__balance-+amount>0:
####            self.__balance-=amount
####
####    def get_balance(self):
####        print(self.__balance)
####
####
####a = BankAccount()
####a.deposit(200)
####
####a.withdraw(300)
####a.get_balance()
##
##
####from math import pi
####
####class Parent:
####
####    def area(self):
####        print("this a parent class method")
####
####class Child(Parent):
####
####    def area(self,r):
####
####        return pi*r*r
####
####class Child2(Parent):
####
####    def area(self,l,w):
####
####        print(l*w)
####
####
####a = Child()
####print(a.area(20))
####
####c = Child2()       
####c.area(30,50)
##
##
####
####from abc import ABC,abstractmethod
####
####
####class Vehicle(ABC):
####
####
####    @abstractmethod
####    def Start(self):
####        pass
####
####class Car(Vehicle):
####
####    def Start(self):
####        print("car is start on time")
####
####a = Car()
####a.Start()
##
##
####class A:
####
####    salary = 2000
####
####    def display(self,name,age):
####        print(f"the instance method name:{name} the age is a:{age}")
####
######     
####    @classmethod
####    class Display(cls):
####        print("the salary is a",cls.salary)
####        
####    def static_method():
####        print("hello guys")
####
####a = A()
####A.static_method()
####
####A.Display()
####a.display("roshan",12)
##
##
####class Father:
####
####    def skills(self):
####        print("father skill :- Driving")
####
####
####class Mother:
####
####    def skills(self):
####        print("mother skills :- ")
####
####class Child(Father,Mother):
####
####    pass
####
####a = Child()
####a.skills()
##
##
####class Details:
####
####    def __init__(self,name):
####        self.name = name
####
####class Student(Details):
####
####    def __init__(self,name,roll_no):
####        super().__init__(name)
####        self.roll_no = roll_no
####
####    def display(self):
####        print(f"Name : - {self.name} the a roll number:-{self.roll_no}")
####
####a = Student("roshan",121)
####
####a.display()
##
##
##
##
##
####class Employee:
####
####    def work(self):
####        print("Employee is Working..............................")
####
####class Student(Employee):
####
####    def work(self):
####
####        super().work()
####
####        print("the student also work hard for joing the big mmc")
####
####a = Student()
####
####a.work()
##
##
####num = [1, 2, 2, 3, 1, 4, 2, 3, 5]
####
####d1 = {}
####
####for i in num:
####    d1[i] = i+1
####
####
####for i in d1.items():
####    print(i)
##
####
####st = "aabbcdde"
####
####for i in st:
####    count = st.count(i)
####
####    if count==1:
####        print(i)
####        break
##
####
####li = [1,24,4,2,34,13,100,1000,1500,3000]
####
####
####a = li.sort(reverse=True)
####
####a = sorted(li)
####
####print(a[-2])
##
##
##
####d1 = {"roshan":99,
####      "tushar":89,
####      "manish":97,
####      "krishna":100
####      }
##
####d = d1.values()
####
######max1 = 0
####
####
####a = sorted(d)
####
####print(a[-1])
##
####
####
####num = 28
####
####
####no = num
####
####rev = 0
####for i in range(0,num,1):
####    a = no // 10
####    rev +=a
####    no = no//10
####
####    
####if rev == num:
####    print("perfact")
####else:
####    print("not",rev)
##    
##
####num = 28
####
####total = 0
####
####for i in range(1,num//2+1):
####    if num%i==0:
####        total+=i
####
####if total==num:
####    print("pefect number")
####else:
####    print("not perfect number")
##
##
##
##
####def factorial(n):
####
####
####    fact = 1
####
####    num = n
####
####
####    for i in range(1,num+1,1):
####        fact*=i
####
####    print(fact)
####
####factorial(9)
####
####num=14
####sum1 = 0
####for i in str(num):
####    sum1+=factorial(int(i))
####
####if num==sum1:
####    print("strong number")
##
##    
##
####
####def strong(n):
####    num = n 
####
####
####    total = 0
####
####    for i in range(1,num):
####        if num%i==0:
####            total+=i
####
####    if total==num:
####        print("perfect number",num)
######    else:
######        print("not a perfect number")
####
####
####
####for i in range(0,1000,1):
####    strong(i)
####
##
##
####num = 15
####
####a1 = len(str(num))
####
####no = num
####
####cube = 0
####        
####for i in range(1,num+1,1):
####        a = no%10
####        cube = cube+a**a1
####        no = no // 10
####
####if num==cube:
####    print("amstrong number")
####else:
####    print("not a")
####        
##
##
####
####li = [1,2,3,5,6,7]
####
####for i in range(1,len(li),1):
####    if i not in li:
####        print(i)
##
####
####st = "madam"
####
####if st==st[::-1]:
####    print("palindrome number")
####else:
####    print("not a pailndrome")
##
####li = [1,2,3,4,5,6,4,5,2,1,2,3,33,122]
####
####
####li1= []
####
####for i in li:
####    if i not in li1:
####        li1.append(i)
####
####print(li1)
##
####li = [2,7,8,9,5,1,5,4,6]
####target = 10
####li1 = []
####for i in range(0,len(li),1):
####    for j in range(i+1,len(li)):
####        if li[i]+li[j]==target:
####            li1.append(li[i])
####
####print(li1)
##
##
##
####li = [2,7,8,2,34,6,1]
####
####target = 9
####li1 = []
####for i in li:
####    for j in range(i+1,len(li)):
####        if i+li[j]==target:
####            li1.append(i)
####            li1.append(j)
####
####print(li1)
##
####
####st = "programming"
####
####for i in range(0,len(st),1):
####    if st[i]=="g":
####        print(i)
##
##
####
####st = "RoshaN"
####
####for i in range(65,90,1):
####    if chr(i) in st:
####        print("ahe re:-",chr(i))
##
##
####
####li = [1,2,3,4,5,6,2,1]
####li1 = []
####for i in li:
####    if li.count(i)>1 and i not in li1:
####        li1.append(i)
####
####print(li1)
##
##
####li = [2,7,90,100,12,12,34]
####li1= []
####target = 24
####for i in range(0,len(li),1):
####    for j  in range(i+1,len(li)):
####        if li[i]+li[j]==24:
####            li1.append(li[i])
####            li1.append(li[j])
####
####print(li1)
##
####
####num = 28
####
####total = 0
####
####for i in range(1,num):
####    if num%i==0:
####        total+=i
####
####if total==num:
####    print("perfect number")
##
##
####li = [120,34,5,6,132,100,1000]
####
####
####a = sorted(li)
####
####print(a[-2])
##
##
####words = ["eat", "tea", "tan",'tae', "ate", "nat", "bat"]
####
####li = []
####li1 = []
####
####for i in range(0,len(words),1):
####    for j in range(0,len(words[i]),1):
####        if words[j] not in li:
####            li.append(words[j])
#### 
####
####    if words[i] not in li:
####        li1.append(words[i])
####
####
####
####print(li)
######
####li3=[]
####
####li3.append([li,li1])
####
####print(li3)
####        
##    
####nums = [1, 1, 1, 2, 2, 3,4,3,5]
####
######li=[]
######li1=[]
######for i in range(len(nums)):
######    count = nums.count(nums[i])
######
######    if count>1:
######        print(nums[i])
######
######print(li)
######        
####
####for i in nums:
####    count = nums.count(i)
####
####    if count==1:
####        print(i)
####        break
##
##
##
##
##
##
##
####
####words = ["eat", "tea", "tan",'tae', "ate", "nat", "bat"]
####
####li = []
####li1 = {}
####
######[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
####
####for i in range(0,len(words),1):
####    for j in range(0,len(words[i]),1):
####        if words[i][j] not in li or words[i][j].startswith(words[j]):
####            li[i]=words[j]
##
##
####print(li)
##
##
####hotel_data = {
####    "what is the hotel name": "Welcome to Royal Palace Hotel.",
####    
####    "where is the hotel located": "Royal Palace Hotel is located in Pune, Maharashtra.",
####    
####    "what rooms are available": "We have Single, Double, Deluxe and Suite rooms.",
####    
####    "what is the single room price": "The Single Room costs Rs. 1500 per night.",
####    
####    "what is the double room price": "The Double Room costs Rs. 2500 per night.",
####    
####    "what is the deluxe room price": "The Deluxe Room costs Rs. 3500 per night.",
####    
####    "what is the suite room price": "The Suite Room costs Rs. 5000 per night.",
####    
####    "what food do you serve": "We serve Veg and Non-Veg food.",
####    
####    "what veg food do you have": "We have Paneer Tikka, Veg Biryani, Masala Dosa and Veg Thali.",
####    
####    "what non veg food do you have": "We have Chicken Biryani, Chicken Tikka, Butter Chicken and Mutton Biryani.",
####    
####    "what are the hotel facilities": "We provide Wi-Fi, parking, room service, restaurant and laundry service.",
####    
####    "is wifi available": "Yes, free Wi-Fi is available for hotel guests.",
####    
####    "is parking available": "Yes, free parking is available for hotel guests.",
####    
####    "what are the check in timings": "Check-in time is 12:00 PM.",
####    
####    "what are the check out timings": "Check-out time is 11:00 AM.",
####    
####    "do you provide room service": "Yes, we provide 24-hour room service.",
####    
####    "how can i book a room": "You can book a room through the hotel reception or booking system.",
####    
####    "how can i cancel my booking": "You can cancel your booking by contacting the hotel reception.",
####    
####    "do you accept online payment": "Yes, we accept online payment, UPI, debit cards and credit cards.",
####    
####    "is breakfast included": "Breakfast is included with Deluxe and Suite room bookings.",
####    
####    "thank you": "You're welcome! Have a pleasant stay.",
####    
####    "hello": "Hello! Welcome to Royal Palace Hotel. How can I help you?"
####}
####
####
####while True:
####    question =input("Ask Question:-").lower()
####
####    if question in hotel_data.keys():
####        print(hotel_data[question])
####    else:
####        print("sorry sir i don't uderstand what you say")
##        
##
##
##
##    
####di = {
####        "roshan pardeshi":"student",
####        "sonu patil":"not student",
####        "tushar patil":"college student"
####    }
##
####li = []
##
####user = input("Enter the :-----")
##
####for i in di.keys():
####    li.append(i)
##
####for i in range(0,len(li),1):
####    if user in li[i]:
####        print(di[li[i]])
##
##
##
##
####li = [7, 1, 5, 3, 6, 4]
####
####
####buy = li[1]
####
####sell = li[5]
####
####print(sell-buy)
##
##
####for i in li:
####    print(i)
##
##
##
####li = [4, 1, 2, 4, 3, 4, 2, 1, 4]
####
####
####
####
####li1 = []
####
####d1 ={}
####for i in li:
####    count = li.count(i)
####    
####    if count>1:
####        if i not in li1:
####            d1[i]=count
####            li1.append(i)
####
####
####print(d1)
##
####li = [4, 1, 2, 4, 3, 4, 2, 1, 4]
####
####li1 = []
####d1 = {}
####
####for i in li:
####    count = li.count(i)
####
####    if count > 1:
####        if i not in li1:
####            d1[i] = count
####            li1.append(i)
####
####most_frequent = None
####frequency = 0
####
####for key, value in d1.items():
####    if value > frequency:
####        frequency = value
####        most_frequent = key
####
####print("Most frequent element:", most_frequent)
####print("Frequency:", frequency)
####
##
####li = [2, 7, 11, 15, 3, 6]
####target = 9
####
####li1 = []
####
####for i in range(0,len(li),1):
####    for j in range(i+1,len(li)):
####        if li[i]+li[j]==target:
####            li1.append((li[i],li[j]))
####
####
####print(li1)
##            
####li = [1, 2, 3, 5, 6, 7, 8, 9]
####
####
####for i in range(1,len(li)+2,1):
####    if i not in li:
####        print(i)
####    
##
##
####li = [3, 1, 4, 1, 5, 9, 2, 6, 5]
####
####for i in li:
####    count = li.count(i)
####
####    if count>1:
####        print(i)
####        break
##
####li = [1, 2, 3, 4, 5, 6, 7]
####
####
####
####li1 = li[-1]
####
####li2 = li[-2]
####
####li3 = li[-3]
####
####li4 = li[-4]
####
####li.pop()
####
####li.pop()
####
####li.pop()
####
####li.pop()
####
####li.insert(0,li4)
####
####li.insert(1,li3)
####
####li.insert(2,li2)
####
####li.insert(3,li1)
####
####print(li)
##
##
##
##
##
##
##
##
##
####
####st = "({[]})"
####
####li = []
####
####for i in st:
####    li.append(i)
####
####
####for i in li:
####
####    if i.isdigit() or i.isalpha():
####        pass
####    else:
####
####        if len(li)==len(st):
####            print("valid")
##
####li = "aabbcdde"
####
####for i in li:
####    count = li.count(i)
####
####    if count==1:
####        print(i)
####        break
##
##
##
####
####li = [1, 2, 3, 4]
####
####for i in range(0,len(li),1):
####    if li[i]:
####        print(li[i])
####
####    else:
####        print(li[i]*4)
##
##
##
####
####class A:
####
####    def no_st(self):
####        print("roshan pardeshi")
####
####a = A()
####a.no_st()
##
##
####
####class A:
####
####    def st():
####        print("static method are exicuted")
####
####A.st()
##
##
####class A:
####
####    a = 10
####
####class B(A):
####
####    def inherit(self):
####        print(self.a)
####
####b=B()
####
####b.inherit()
##
##
##
####class A:
####
####    def show(self):
####        print("class A")
####
####class B(A):
####
####    def show1(self):
####        print("hi class b class")
####
####
####class C(B):
####
####    def show2(self):
####        print("class c class")
####
####
####c = C()
####
####c.show()
####c.show1()
####c.show2()
##
##
##
##
####class A:
####
####    def show(self):
####        print("class A method")
####
####class B(A):
####
####    pass
####
####class C(A):
####    pass
####
####c = C()
####c.show()
####
####b = B()
####b.show()
##
##
##
####class A:
####
####    def show(self):
####        print("class A method")
####
####class B:
####
####    def show2(self):
####        print("class B method")
####
####class C(A,B):
####    pass
####
####c = C()
####c.show()
####c.show2()
##
##
##
####class A:
####
####    def show(self):
####        print("class A method")
####
####class B(A):
####
####    def show1(self):
####        print("class B method")
####
####class C(A):
####
####    def show2(self):
####        print("class C method")
####
####
####class D(C,B):
####
####    pass
####
####d = D()
####d.show()
####d.show1()
####d.show2()
##
##
##
##
####class A:
####
####    def __init__(self,name,age,address):
####        self.name = name
####        self.age = age
####        self.address = address
####
####
####    def __str__(self):
####        return f" Name :- {self.name}  Age :- {self.age} Address :- {self.address}"
####
####n = int(input("enter how many student you try to add"))
####li = []
####
####for i in range(n):
####    a = A(input("enter the name"),int(input("enter the age")),input("enter the a address"))
####    li.append(a)
####
####
####for i in li:
####    print(i)
##
##
##
####class A:
####
####    a = 10
####    _b = 20
####    __c = 30
####
####
####    def show(self):
####        print("Local variable:-",self.a,"protected variable:-",self._b,"private variable:-",self.__c)
####
####
####    def _show1(self):
####        print("private variable:-",self.__c)
####
####
####    def __show3(self):
####        print("use the a protected variable:--",self._b)
####
####
####    def getter(self):
####        self.__show3()
####
####a = A()
####a.show()
####a.getter()
####a._show1()
##
##        
##
####from abc import ABC,abstractmethod
####
####class A(ABC):
####
####    @abstractmethod
####    def show(self):
####        pass
####
####    @abstractmethod
####    def show1(self):
####        pass
####
####
####class B(A):
####
####    def show(self):
####        print("first abstract method:-")
####
####    def show1(self):
####        print("second abstract method:-")
####
####
####b = B()
####b.show()
####b.show1()
##
##
##
####from multipledispatch import dispatch
####
####class A:
####
####    @dispatch(int,int)
####    def show(self,a,b):
####        print("value of a:-",a,"value of B:-",b)
####
####        
####    @dispatch(int,int,int)
####    def show(self,a,b,c):
####        print("adition is a:-",a+b+c)
##
##
####a = A()
####a.show(10,20)
####a.show(10,20,30)
##
##
####
####from math import *
####
####from math import pi
####
####
####import math
####
####from math import factorial
##
##
##
####s1 = {1,2,3,4,5,4,5,1}
####
####
####s2 = {4,5,6,7,8,9,10}
####
####
####print("UNION :-",s1.union(s2))
####
####print("INTERSECTION :-",s1.intersection(s2))
####
####print("DIFFERENCE :-",s1.difference(s2))
####
####
####print("SYMMETRIC DIFFERENCE :-",s1.symmetric_difference(s2)) 
####
####print("COMPLETE SET FISRT:-",s1,s2)
##
####
####
####d1 = {
####    "name":"roshan",
####    "age":21,
####    "address":"kasba",
####    "roll_no" :27
####    }
####
####
####print(d1.values())
##
##
####li = [10, 25, 30, 45, 50, 65, 70, 85]
####
####b = len(li)
####
####a = 0
####
####for i in li:
####    a+=i
####    c = a / b
####
####
####
####for i in li:
####    if i>c:
####        print(i)
####    
##
##
##
####li = [10, 20, 10, 30, 20, 40, 10, 50]
####
####li1=[]
####for i in li:
####    count = li.count(i)
####
####    if count>1:
####        if i not in li1:
####            li1.append(i)
####
####
####print(li1)
##
##
####li = ["eat", "tea", "tan", "ate", "nat", "bat"]
####
####
####for i in range(0,len(li),1):
####    for j in range(i+1,len(li)):
######        print(li[i])
####        if j in li[i]:
####            print(li[j])
##
##
####li = [4, 7, 2, 8, 4, 9, 2, 1, 7, 5]
####
####for i in li:
####    count = li.count(i)
####
####    if count==1:
####        print(i)
####        break
####
####li = [1, 2, 3, 4, 5, 6, 7, 8]
####
####li1 = []
####for i in range(0,len(li),1):
####    for j in range(i+1,len(li)):
####        if li[i]+li[j]==9:
####            li1.append((li[i],li[j]))
####
####
####print(li1)
##        
##
##
##
####li = [1,2,3,4,5,8,9,10]
####
####
####
####
####for i in range(1,len(li)+2,1):
####    if i not in li:
####        print(i)
##              
##
##
##
####li1 = [10, 20, 4, 45, 99, 67, 99, 45]
####li = []
####
####for i in li1:
####    if i not in li:
####        li.append(i)
####
####
####
####
####max1 = li[0]
####
####for i in li:
####    if max1<i:
####        max1=i
####
####li.remove(max1)
####max2 = li[0]
####for i in li:
####    if max2<i:
####        max2=i
####
####
####li.remove(max2)
####max3 = li[0]
####for i in li:
####    if max3<i:
####        max3=i
####
####
####
####print(max3)
##
####li = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
####li1 = []
####for i in li:
####    count = li.count(i)
####
####    if count>1:
####        li1.append(i)
####
####
####print(li1[1])
##
##
##
####li= [10, 20, 30, 40, 50]
####
######print(li[::-1])
####
####
####li.sort(reverse=True))
##
####
####li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
####
####li1 = []
####li2 =[]
####
####for i in li:
####
####    if i%2==0:
####        li1.append(i)
####    else:
####        li2.append(i)
####
####print("EVEN:-",li1)
####
####print("ODD",li2)
##
##
##
##
####li = [5, 2, 8, 2, 9, 1, 5, 8, 3]
####
####li1 = []
####
####for i in li:
####    count = li.count(i)
####
####    if i not in li1:
####        print(i," : ",count)
####        li1.append(i)
##
##
####li = [10, 20, 30, 50, 60]
##
####for i in range(li[0],len(li),1):
####    print(li[i])
####
##
####
####li.pop(3)
####
####print(li)
##
##
####li = [45, 12, 78, 3, 25, 9]
####
####
####max1 = li[0]
####
####for i in li:
####    if max1>i:
####        max1=i
####
####print(max1)
##
##
##
##
##
####li = [10, 50, 20, 80, 40, 70]
####
####
####max1 = li[0]
####
####
####for i in li:
####    if max1<i:
####        max1=i
####li.remove(max1)
####
####max2 = li[0]
####
####for i in li:
####    if max2<i:
####        max2 = i
####
####print(i)
##    
##
####st = "programming"
####
####li = ""
####
####for i in st:
####    count = st.count(i)
####
####    if i not in li:
####        print(i,":",count)
####        li+=i
##
##    
####text = "aabbcde"
####
####for i in text:
####    count = text.count(i)
####
####    if count==1:
####        print(i)
####        break
##
##
##
##
####text = "madam"
####
####
####res = ""
####
####for i in range(len(text)-1,-1,-1):
####    res+=text[i]
####
####if res == text:
####    print("palindrome")
##
##
##
####li  = [45, 12, 78, 3, 25, 9]
####
####
####min1 = li[0]
####
####for i in li:
####    if min1>i:
####        min1=i
####
####li.remove(min1)
####
####min2 = li[0]
####
####for i in li:
####    if min2>i:
####        max2=i
####
####print(max2)
##
##
####li = [1, 2, 2, 3, 4, 4, 5]
####
####li2 = []
####
####for i in li:
####    if i not in li2:
####        li2.append(i)
####
####print(li2)
##
##
##
####li = [10, 20, 30, 40, 50]
####
####
####sum1=0
####
####for i in li:
####    sum1+=i
####
####print(sum1)
##
##
##
##
####li = [10, 25, 30, 45, 50, 65]
####
####
####sum1 = 0
####
####s = len(li)
####
####for i in li:
####    sum1+=i
####
####print(sum1/s)
##
##
##
####li = [10, 15, 20, 25, 30, 35]
####
####
####count_even = 0
####
####count_odd = 0
####
####for i in li:
####    if i%2==0:
####        count_even+=1
####
####    else:
####        count_odd+=1
####
####print(count_even)
####
####print(count_odd)
##
##
##        
####
####li = [10, 20, 10, 30, 20, 40, 50, 30]
####
####
####li1 = []
####
####li2 = []
####
####for i in li:
####    if i not in li1:
####        li1.append(i)
####    else:
####        li2.append(i)
####
####print(li2[0])
##    
####
####li = [1, 2, 3, 4, 5, 6, 7]
####li1=[]
####target = 7
####for i in range(0,len(li),1):
####    for j in range(i+1,len(li)):
####        if li[i] + li[j] == target:
####            li1.append((li[i],li[j]))
####
####print(li1)
##
##
####li = [1, 2, 3, 4, 5]
####
####li1 = li[-1]
####
####li.pop()
####
####li.insert(0,li1)
####
####print(li)
####
####
####
##
##
##
####
####li = [0,1, 0,2, 3, 4, 5, 6]
####
####
####zeros = 0
####
####li1 = []
####
####for i in li:
####    if i==0:
####        zeros+=1
####
####    else:
####        li1.append(i)
####
####for i in range(zeros):
####    li1.append(0)
####
####print(li1)
##
##
####li = [1, 2, 3, 2, 4, 1, 5, 3]
####
####
####for i in li:
####    count = li.count(i)
####
####
####    if count==1:
####        print(i)
####        break
##
####li = [1, 2, 3, 4, 5, 6]
####
####
####for i in range(1,len(li)+2,1):
####    if i not in li:
####        print(i)
##
##
##
##
####li = [10, 50, 20, 80, 40, 70]
####
####
####max1 = li[0]
####
####for i in li:
####    if max1<i:
####        max1=i
####
####print("maximum number:-",max1)
####
####li.remove(max1)
####
####max2 = li[0]
####
####for i in li:
####    if max2<i:
####        max2=i
####
####print("second maximum:-",max2)
##
##
##
##
##
####li = [10, 20, 30, 40, 50]
####
####for i in range(len(li)-1,-1,-1):
####    print(li[i])
##
##
##
####li=[1, 2, 3, 4, 5, 6]
####
####li1 = []
####li2 = []
####li3=[]
####for i in li:
####    if i%2==0:
####        li1.append(i)
####    else:
####        li2.append(i)
####
####
####
####li3.append(li1)
####
####li3.append(li2)
####
####
####print(li3)
##
##
##
##li = [1, 2, 2, 3, 4, 4, 5, 5, 5]
##
##
####
####li1=[]
####
####for i in li:
####    count = li.count(i)
####
####    if count>1:
####        if i not in li1:
####            li1.append(i)
####
####print(li1)
####    
##
##
####
####li = [10, 20, 30, 40, 50]
####
####
####li1 = li[-1]
####
####li2 = li[0]
####
####
####li.pop()
####
####li.remove(li2)
####
####li.insert(0,li1)
####
####li.extend([li2])
####
####
####print(li)
##
##
##
##
##
##
##
##
####
####li = [10, 20, 30, 40, 50]
####
####li[0],
####li[-1] = li[-1],
####li[0]
####
####print(li)
##
##
##
####li = [10, 20, 30, 40, 50]
####
####for i in range(0,len(li),1):
####    if li[i]==30:
####        print(i)
##
##
##
####li = [10, 20, 30, 40, 50]
####
####
####target = 30
####
####for i in li:
####    if i==target:
####        print("found")
####        break
##
##
##
####x = 10
####y = 20
####
####res = calculate(x, y)
####
####print(res)
####
##
##
##
####
####li = [10, 20, 30, 40, 50]
####
####
####
####for i in range(len(li)-1,-1,-1):
####    print(li[i])
####
##
##
##
##
####li = [2, 7, 11, 15, 3, 6]
####target = 9
####
####li1 = [] 
####for i in range(0,len(li),1):
####    for j in range(i+1,len(li)):
####        if li[i]+li[j]==target:
####            li1.append([li[i],li[j]])
####
####
####print(li1)
####        
##
##
####
####li = [1, 2, 3, 4, 5, 6, 7]
####
####
####
####
####
######li2 = [li,li[-3],li[-2],li[-1]]
####
######print(li2)
####
####li2 = []
####
####k=4
####
####for i in range(k,len(li),1):
####        li2.append(li[i])
####        
####for i in range(k-1):
####    li.pop()
####
####
####
####for i in range(0,len(li2),1):
####    li.insert(i,li2[i])
####
####print(li)
##
##
##
##
##
##
####
####li = [1, 2, 2, 3, 4, 4, 5, 2, 6]
####
####li2 = []
####
####for i in li:
####    if i not in li2:
####        li2.append(i)
####
####print(li2)
####    
####
####arr = [1, 2, 3, 5, 6]
####
####
####
####for i in range(1,len(arr)+2,1):
####    if i not in arr:
####        print(i)
##
##
####li = [1, 2, 3, 4, 5, 6, 7]
####k = 3
####
####li2 = []
####
####for i in range(len(li) - k, len(li)):
####    li2.append(li[i])
####
####for i in range(len(li) - k):
####    li2.append(li[i])
####
####print(li2)
####
##
####arr1 = [10, 5, 20, 8, 20, 15]
####
####
####arr = []
####for i in arr1:
####    if i not in arr:
####        arr.append(i)
####    
####
####
####maximum_first = arr[0]
####
####
####maximum_second = arr[0]
####
####
####for i in arr:
####    if maximum_first<i:
####        maximum_first=i
####
####arr.remove(maximum_first)
####
####for i in arr:
####    if maximum_second<i:
####        maximum_second=i
####
####print(maximum_second)
##
##
##
####arr = [0, 1, 0, 00,3, 12,0,00,00]
####
####
####count = 0
####
####li2 = []
####for i in arr:
####    if i==0:
####        count+=1
####    else:
####        li2.append(i)
####
####for i in range(count):
####    li2.append(0)
####
####print(li2)
##
####
####arr1 = [1, 2, 3, 4, 5, 6,10]
####arr2 = [4, 5, 6, 7, 8, 9,10]
####
####arr3 = []
####for i in arr1:
####    if i in arr2:
####        arr3.append(i)
####
####print(arr3)
##
##
##
####arr = [1, 2, 2, 3, 1, 4, 2, 3, 5]
####
####
####arr2 = []
####
####for i in arr:
####    count = arr.count(i)
####
####    if i not in arr2:
####        print(i," : ",count)
####        arr2.append(i)
##
##
####arr = [10, 5, 3, 4, 3, 5, 6]
####
####arr2 = []
####for i in arr:
####    if i not in arr2:
####        arr2.append(i)
####    else:
####        print(i)
####        break





arr = [1, 2, 2, 3, 4, 3, 5, 1]


##num = len(arr)
##
##i = 0
##
##while arr>i:
##    print(i)
##    i+=1
##arr = [1, 2, 2, 3, 4, 3, 5, 1]
##
##i = 0
##
##while i < len(arr):
##    j = i + 1
##
##    while j < len(arr):
##        if arr[i] == arr[j]:
##            arr.pop(j)
##        else:
##            j += 1
##
##    i += 1
##
##print(arr)
##
##i=0
##
##while len(arr)>i:
##
##    j = i+1
##
##    while j<len(arr):
##
##            if arr[i]==arr[j]:
##                arr.pop(j)
##            else:
##                j+=1
##    
##    i+=1
##
##
##print(arr)






##
##li = [1, -2, 3, -4, 5, -6, 7]
##
##li2 = []
##
##li3 = []
##for i in li:
##    if i<0:
##        li2.append(i)
##    else:
##        li3.append(i)
##
##
##li4 = li2+li3
##
##print(li4)


##
##li = [1, 2, 2, 3, 4, 3, 5, 1]
##
##
##for i in range(0,len(li),1):
##    for j in range(i+1,len(li),1):
##        if i==j:
##            li.pop(li[j])
##        else:
##            li[j]+=1
##
##print(li





##li = [-10, -3, 5, 6, -2]
##
##
##li2 = li[0]*li[1]
##print(li2)
##
##li3 = []
##for i in range(0,len(li),1):
##    for j in range(i+1,len(li)):
##        if li[i]*li[j]>li2:
##            li3.append([li[i],li[j]])
##
##print(li3)




##
##
##li = [2, 2, 1, 1, 1, 2, 2]
##
##li1 = 0
##for i in li:
##    count = li.count(i)
##
##    if count>1:
##        if count>li1:
##            li1=i
##
##
##print(li1)



##
##class InvalidageError(Exception):
##    pass
##
##
##try:
##    age = int(input("enter the age:--"))
##
##    if age<18:
##        raise InvalidageError
##
##except InvalidageError:
##    print("error")
##
##else:
##    print(age)
##    


##class NegativeNumberError(Exception):
##    pass
##
##
##try :
##    a = int(input("enter the number"))
##
##    if a<0:
##        raise NegativeNumberError
##
##except NegativeNumberError:
##    print("Negative number exception")
##
##else:
##    print("the a :-",a)


##class InvalidMarksError(Exception):
##    pass
##
##try:
##
##    marks = int(input("enter the values:--"))
##
##    if marks<0 or marks>100:
##        raise InvalidMarksError
##
##except InvalidMarksError:
##    print("invalid marks")
##
##else:
##    print(marks)


##
##class insuficientBalanceError(Exception):
##    pass
##
##try:
##    balance = 10000
##
##    withdraw = int(input("enter the a withdraw amount"))
##
##    if withdraw<balance:
##        pass
##    else:
##        raise insuficientBalanceError
##
##
##except insuficientBalanceError:
##    print("insuficient balance")
##
##
##else:
##    print("suficient balance",balance-withdraw)


##class Invalidpassword(Exception):
##    pass
##
##try:
##    password = "123456789"
##
##    if len(password)>8:
##        raise Invalidpassword
##
##    
##
##except Invalidpassword:
##    print("invalid password")



##
##try:
##
##    a = 10
##    b = 0
##
##    print(a/b)
##
##except ZeroDivisionError:
##    print("the zero division error occurs")
##
##else:
##    print("a : b")

##
##class NumberNotFoundError(Exception):
##    pass
##
##
##try:
##    li = [1,2,3,4,5,6,7,8]
##
##    user = int(input("enter the number"))
##
##    if user not in li:
##        raise NumberNotFoundError
##
##
##except NumberNotFoundError:
##    print("number not found error ouccrs")
##
##else:
##    print("the number is a",user)
##        


##
##
##class DuplicateValueError(Exception):
##    pass
##
##
##try:
##
##    li = [1,2,3,4]
##
##    for i in li:
##        count = li.count(i)
##
##    if count>1:
##        raise DuplicateValueError
##
##except DuplicateValueError:
##    print("duplicates are avilable")
##
##else:
##    print(count)

##class InvalidUsernameError(Exception):
##    pass
##
##
##
##try:
##
##    username = "roshan pardeshi"
##
##
##    for i in username:
##        if i==" " or len(i)>5:
##            raise InvalidUsernameError
## 
##except InvalidUsernameError:
##    print("username error")
##
##else:
##    print(username)
##
##class lessSalaryError(Exception):
##    pass
##
##try:
##    salary = 1500
##
##    if salary<15000:
##        raise lessSalaryError
##
##
##except lessSalaryError:
##    print("less salary error occurs")
##else:
##    print(salary)

##
##class InsuficientMarksError(Exception):
##    pass
##
##
##try:
##
##    a = 40
##    b = 31
##    c = 45
##    d = 50
##    e = 51
##
##    if a<35 or b<35 or c<35 or d<35 or e<35:
##        raise InsuficientMarksError
##
##except InsuficientMarksError:
##    print("the error are ouccrs")
##
##else:
##    print("pass")

##class LoginFailedError(Exception):
##    pass
##
##try:
##
##    username = "roshan"
##
##    password = 1234
##
##    for i in range(3):
##        user = input("enter the username")
##        passw = int(input("enter the password"))
##
##        if user==username and passw==password:
##            pass
##        else:
##            raise LoginFailedError
##
##except LoginFailedError:
##    print("error")
                    

                    
##li = [1,2,3,4,5,6,7,8,9]
##
##res = list(map(lambda x:x**2,li))
##
##print(res)
##
##res = list(map(lambda x:x*2,li))
##
##print(res)

##li = ["roshan","vijay","pardeshi"]

##res = list(map(lambda x:str(x),li))
##
##print(res)

##res = list(map(lambda x:x.upper(),li))
##
##print(res)

##price = [100,200,300,400,500]
##
##res= list(map(lambda x:x+(x*18/100),price))
##
##print(res)

##li = [1,2,3]
##
##li1 = [4,5,6]
##
##res = list(map(lambda x:x+li1,li))
##
##print(res)




##li = [1,2,3,4,5,6,7,8,9,10]

##res = list(filter(lambda x:x%2==0,li))
##
##print(res)

##res = list(filter(lambda x:x%2!=0,li))
##
##print(res)

##
##li = [10,20,30,40,50,60,70,80,90,100]
##
##res = list(filter(lambda x:x>50,li))
##
##print(res)

##
##li = [1,2,-3,4,-5,6,-7]
##
##res = list(filter(lambda x:x>0,li))
##
##print(res)

##li = ["roshan","nanda","vijay","pardeshi"]
##
##
##res = list(filter(lambda x:len(x)>5,li))
##
##print(res)
##
##
##li = [1,2,3,4,5,6,7,8,9,10,15]
##
##res = list(filter(lambda x:x%3==0 and x%5==0,li))
##
##print(res)
##
##li = [1,2,3,4,5,6,7,8,9,10]
##
##res = list(filter(lambda x:x%2==0,li))
##
##res1 = list(map(lambda x:x**2,res))
##
##print(res1)
##
##li = [100,2000,40000,50000,1000000]
##
##res = list(filter(lambda x:x>30000,li))
##
##res1 = list(map(lambda x:x+(x*10/100),res))
##
##print(res1)


##li = ["roshan","sonu","pardeshi","monu","nanda","dhanger"]
##
##
##res = list(filter(lambda x:len(x)>4,li))
##
##res1 = list(map(lambda x:x.upper(),res))
##
##print(res1)


##li = [1,2,-3,4,-5,6,-7,-8]
##
##res = list(filter(lambda x:x%2==0,li))
##
##res1 = list(map(lambda x:x**x,res))
##
##print(res1)


##li = [10,20,40,50,60,70,100]
##
##res = list(filter(lambda x:x==40,li))
##
##res1 = list(map(lambda x:x+5,res))
##
##print(res1)


##
##li = [10, 15, 20, 25, 30, 35, 40, 45, 50]
##
##li1 = list(filter(lambda x:x>20 and x%2==0,li))
##
##res = list(map(lambda x:x**2,li1))
##

##print(res)


import numpy as np

##li = [10,20,30,40,50]
##
##arr = np.array(li)
##
##print(arr)

##arr = np.arange(1,21,1)
##
##print(arr)
##
##%%timeit

##arr = np.zeros(10)
##
##print(arr)


##arr1 = np.ones(10)
##
##print(arr1)


##li = [1,2,3,4,5,6,7,8,9,10]
##
##
##
##arr = np.array(if li%2==0)
##
##print(arr)



from multipledispatch import dispatch


class A:

    @dispatch(int,int)
    def show(a,b):
        print("Addition:--",a+b)

    @dispatch(int,int,int)
    def show(a,b,c):
        print("addition of three:--",a+b+c)

##a = A()
##a.show(10,30)
##a.show(10,20,30)
##
##
##st = "roshan"
##print(st+"shonu")


##
##from abc import ABC,abstractmethod
##
##
##
##class A(ABC):
##
##    @abstractmethod
##    def B(self):
##        pass
##
##    @abstractmethod
##    def C(self):
##        pass
##
##class E(A):
##
##    def B(self):
##        print("Roshan")
##
##    def C(self):
##        print("Pardeshi")
##
##x = E()
##
##x.B()
##x.C()



##class A:
##
##    def static():
##        print("static class")
##
##    def non_static(self):
##        print("non static method")
##
##a = A()
##A.static()
##a.non_static()



##class A:
##
##    def show(self):
##        print("Class A")
##
##class B(A):
##
##    def show2(self):
##
##        print("Class B")
##
##b =B()
##b.show()
##b.show2()



##class A:
##
##    a = 20
##    _b = 30
##    __c = 40
##
##    def show(self):
##        print(self.a+self._b+self.__c)
##
##    def _show1(self):
##        print("protected method")
##        self.__show2()
##
##    def __show2(self):
##        print("Private method")
##        
##
##
##c = A()
##c.show()
##c._show1()





##
##li = [10,20,30,40,50,60,70]
##
##
##max1 = li[0]
##
##for i in li:
##    if max1<i:
##        max1=i
##
##li.remove(max1)
##
##max2 = li[0]
##
##for i in li:
##    if max2<i:
##        max2=i
##
##        
##print(max2)

##st = "datascience"
##st1 = ""
##for i in st:
##    count = st.count(i)
##
##    if i not in st1:
##        print(i,":",count)
##        st1+=i


##
##li = [1,2,3,4,5,6,7,3,1,2,3]
##
##li1 = []
##
##for i in li:
##    if i not in li1:
##        li1.append(i)
##
##
##print(li1)



##li = [1,2,3,4,5]
##li2 = [4,5,6,7,8]
##
##
##
##for i in li:
##    if i in li2:
##        print(i)


##
##st = "madam"
##
##
##if st==st[::-1]:
##    print("palindrome")
##
##num = 112
##
##num = str(num)
##
##if num==num[::-1]:
##    print("palinfrome")
##    


##
##st = "python use for datascience python"
##st = st.split()
##d1 = {}
##
##for i in st:
##    count = st.count(i)
##    d1[i]=count
##
##print(d1)





li = [1,2,3,5,6,7,8,9,10]


even = []
odd = []


for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)


print("even:--",even)
print("odd:---",odd)






import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])




print(arr.mean())

print(np.median(arr))


print(max(arr))

print(min(arr))

print(np.var(arr))
print(np.std(arr))

print(arr>40)

##
##for i in arr:
##    if i>50:
##        i=100

arr = np.random.randint(1,9,(3,3))

print(arr)





















