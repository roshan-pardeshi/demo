

##class Student:
##
##    name = "roshan"
##    age  = 21
##    address = "kusumba"
##
##    def display(self):
##        print(f"the student name:{self.name}the a age is a:{self.age} the address is a:-{self.address}")
##
##a = Student()
##a.display()
##
##b = Student()
##b.display()
####              
##
##class Employee:
##
##    name = "Roshan"
##    salary = 21000
##
##    def display(self):
##        print(f"the Name of employee is a:{self.name} the salary of employee:{self.salary}")
##
##
##class Developer(Employee):
##
##    language = "English"
##
##    def display_developer_details(self):
##
##        print(f"Name:{self.name} the a salary:{self.salary} the language:{self.language}")
##
##a = Developer()
##a.display()##
##a.display_developer_details()


##
##
##class Animal:
##
##    def sound(self):
##        print("the animal sound")
##
##class Dog(Animal):
##
##    def sound(self):
##        print("dog bark")
##
##
##a = Dog()
##
##a.sound()



##class BankAccount:
##
##    account_number = 123456
##
##    __balance = 100000
##
##
##    def deposit(self,amount):
##
##        self.__balance+=amount
##
##
##    def withdraw(self,amount):
##        if self.__balance-+amount>0:
##            self.__balance-=amount
##
##    def get_balance(self):
##        print(self.__balance)
##
##
##a = BankAccount()
##a.deposit(200)
##
##a.withdraw(300)
##a.get_balance()


##from math import pi
##
##class Parent:
##
##    def area(self):
##        print("this a parent class method")
##
##class Child(Parent):
##
##    def area(self,r):
##
##        return pi*r*r
##
##class Child2(Parent):
##
##    def area(self,l,w):
##
##        print(l*w)
##
##
##a = Child()
##print(a.area(20))
##
##c = Child2()       
##c.area(30,50)


##
##from abc import ABC,abstractmethod
##
##
##class Vehicle(ABC):
##
##
##    @abstractmethod
##    def Start(self):
##        pass
##
##class Car(Vehicle):
##
##    def Start(self):
##        print("car is start on time")
##
##a = Car()
##a.Start()


##class A:
##
##    salary = 2000
##
##    def display(self,name,age):
##        print(f"the instance method name:{name} the age is a:{age}")
##
####     
##    @classmethod
##    class Display(cls):
##        print("the salary is a",cls.salary)
##        
##    def static_method():
##        print("hello guys")
##
##a = A()
##A.static_method()
##
##A.Display()
##a.display("roshan",12)


##class Father:
##
##    def skills(self):
##        print("father skill :- Driving")
##
##
##class Mother:
##
##    def skills(self):
##        print("mother skills :- ")
##
##class Child(Father,Mother):
##
##    pass
##
##a = Child()
##a.skills()


##class Details:
##
##    def __init__(self,name):
##        self.name = name
##
##class Student(Details):
##
##    def __init__(self,name,roll_no):
##        super().__init__(name)
##        self.roll_no = roll_no
##
##    def display(self):
##        print(f"Name : - {self.name} the a roll number:-{self.roll_no}")
##
##a = Student("roshan",121)
##
##a.display()





##class Employee:
##
##    def work(self):
##        print("Employee is Working..............................")
##
##class Student(Employee):
##
##    def work(self):
##
##        super().work()
##
##        print("the student also work hard for joing the big mmc")
##
##a = Student()
##
##a.work()


##num = [1, 2, 2, 3, 1, 4, 2, 3, 5]
##
##d1 = {}
##
##for i in num:
##    d1[i] = i+1
##
##
##for i in d1.items():
##    print(i)

##
##st = "aabbcdde"
##
##for i in st:
##    count = st.count(i)
##
##    if count==1:
##        print(i)
##        break

##
##li = [1,24,4,2,34,13,100,1000,1500,3000]
##
##
##a = li.sort(reverse=True)
##
##a = sorted(li)
##
##print(a[-2])



##d1 = {"roshan":99,
##      "tushar":89,
##      "manish":97,
##      "krishna":100
##      }

##d = d1.values()
##
####max1 = 0
##
##
##a = sorted(d)
##
##print(a[-1])

##
##
##num = 28
##
##
##no = num
##
##rev = 0
##for i in range(0,num,1):
##    a = no // 10
##    rev +=a
##    no = no//10
##
##    
##if rev == num:
##    print("perfact")
##else:
##    print("not",rev)
    

##num = 28
##
##total = 0
##
##for i in range(1,num//2+1):
##    if num%i==0:
##        total+=i
##
##if total==num:
##    print("pefect number")
##else:
##    print("not perfect number")




##def factorial(n):
##
##
##    fact = 1
##
##    num = n
##
##
##    for i in range(1,num+1,1):
##        fact*=i
##
##    print(fact)
##
##factorial(9)
##
##num=14
##sum1 = 0
##for i in str(num):
##    sum1+=factorial(int(i))
##
##if num==sum1:
##    print("strong number")

    

##
##def strong(n):
##    num = n 
##
##
##    total = 0
##
##    for i in range(1,num):
##        if num%i==0:
##            total+=i
##
##    if total==num:
##        print("perfect number",num)
####    else:
####        print("not a perfect number")
##
##
##
##for i in range(0,1000,1):
##    strong(i)
##


##num = 15
##
##a1 = len(str(num))
##
##no = num
##
##cube = 0
##        
##for i in range(1,num+1,1):
##        a = no%10
##        cube = cube+a**a1
##        no = no // 10
##
##if num==cube:
##    print("amstrong number")
##else:
##    print("not a")
##        


##
##li = [1,2,3,5,6,7]
##
##for i in range(1,len(li),1):
##    if i not in li:
##        print(i)

##
##st = "madam"
##
##if st==st[::-1]:
##    print("palindrome number")
##else:
##    print("not a pailndrome")

##li = [1,2,3,4,5,6,4,5,2,1,2,3,33,122]
##
##
##li1= []
##
##for i in li:
##    if i not in li1:
##        li1.append(i)
##
##print(li1)

##li = [2,7,8,9,5,1,5,4,6]
##target = 10
##li1 = []
##for i in range(0,len(li),1):
##    for j in range(i+1,len(li)):
##        if li[i]+li[j]==target:
##            li1.append(li[i])
##
##print(li1)



##li = [2,7,8,2,34,6,1]
##
##target = 9
##li1 = []
##for i in li:
##    for j in range(i+1,len(li)):
##        if i+li[j]==target:
##            li1.append(i)
##            li1.append(j)
##
##print(li1)

##
##st = "programming"
##
##for i in range(0,len(st),1):
##    if st[i]=="g":
##        print(i)


##
##st = "RoshaN"
##
##for i in range(65,90,1):
##    if chr(i) in st:
##        print("ahe re:-",chr(i))


##
##li = [1,2,3,4,5,6,2,1]
##li1 = []
##for i in li:
##    if li.count(i)>1 and i not in li1:
##        li1.append(i)
##
##print(li1)


##li = [2,7,90,100,12,12,34]
##li1= []
##target = 24
##for i in range(0,len(li),1):
##    for j  in range(i+1,len(li)):
##        if li[i]+li[j]==24:
##            li1.append(li[i])
##            li1.append(li[j])
##
##print(li1)

##
##num = 28
##
##total = 0
##
##for i in range(1,num):
##    if num%i==0:
##        total+=i
##
##if total==num:
##    print("perfect number")


##li = [120,34,5,6,132,100,1000]
##
##
##a = sorted(li)
##
##print(a[-2])


##words = ["eat", "tea", "tan",'tae', "ate", "nat", "bat"]
##
##li = []
##li1 = []
##
##for i in range(0,len(words),1):
##    for j in range(0,len(words[i]),1):
##        if words[j] not in li:
##            li.append(words[j])
## 
##
##    if words[i] not in li:
##        li1.append(words[i])
##
##
##
##print(li)
####
##li3=[]
##
##li3.append([li,li1])
##
##print(li3)
##        
    
##nums = [1, 1, 1, 2, 2, 3,4,3,5]
##
####li=[]
####li1=[]
####for i in range(len(nums)):
####    count = nums.count(nums[i])
####
####    if count>1:
####        print(nums[i])
####
####print(li)
####        
##
##for i in nums:
##    count = nums.count(i)
##
##    if count==1:
##        print(i)
##        break







##
##words = ["eat", "tea", "tan",'tae', "ate", "nat", "bat"]
##
##li = []
##li1 = {}
##
####[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
##
##for i in range(0,len(words),1):
##    for j in range(0,len(words[i]),1):
##        if words[i][j] not in li or words[i][j].startswith(words[j]):
##            li[i]=words[j]


##print(li)


hotel_data = {
    "what is the hotel name": "Welcome to Royal Palace Hotel.",
    
    "where is the hotel located": "Royal Palace Hotel is located in Pune, Maharashtra.",
    
    "what rooms are available": "We have Single, Double, Deluxe and Suite rooms.",
    
    "what is the single room price": "The Single Room costs Rs. 1500 per night.",
    
    "what is the double room price": "The Double Room costs Rs. 2500 per night.",
    
    "what is the deluxe room price": "The Deluxe Room costs Rs. 3500 per night.",
    
    "what is the suite room price": "The Suite Room costs Rs. 5000 per night.",
    
    "what food do you serve": "We serve Veg and Non-Veg food.",
    
    "what veg food do you have": "We have Paneer Tikka, Veg Biryani, Masala Dosa and Veg Thali.",
    
    "what non veg food do you have": "We have Chicken Biryani, Chicken Tikka, Butter Chicken and Mutton Biryani.",
    
    "what are the hotel facilities": "We provide Wi-Fi, parking, room service, restaurant and laundry service.",
    
    "is wifi available": "Yes, free Wi-Fi is available for hotel guests.",
    
    "is parking available": "Yes, free parking is available for hotel guests.",
    
    "what are the check in timings": "Check-in time is 12:00 PM.",
    
    "what are the check out timings": "Check-out time is 11:00 AM.",
    
    "do you provide room service": "Yes, we provide 24-hour room service.",
    
    "how can i book a room": "You can book a room through the hotel reception or booking system.",
    
    "how can i cancel my booking": "You can cancel your booking by contacting the hotel reception.",
    
    "do you accept online payment": "Yes, we accept online payment, UPI, debit cards and credit cards.",
    
    "is breakfast included": "Breakfast is included with Deluxe and Suite room bookings.",
    
    "thank you": "You're welcome! Have a pleasant stay.",
    
    "hello": "Hello! Welcome to Royal Palace Hotel. How can I help you?"
}




while True:
    question =input("Ask Question:-").lower()

    if question in hotel_data.keys():
        print(hotel_data[question])
    else:
        print("sorry sir i don't uderstand what you say")
        
    



































