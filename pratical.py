

##class A:
##
##    __pin = 1234
##
##    balance = 10000
##
##
##    def set_pin(self,new_pin):
##        if len(str(new_pin))==4:
##            self.__pin=new_pin
##            print("pin set successfully")
##
##        else:
##            print("your pin length is larger")
##
##
##    def valid_pin(self,a):
##        if self.__pin==a:
##            print("correct pin")
##        else:
##            print("wrong pin")
##
##    def __display(self,a):
##        if self.__pin==a:
##            print(self.balance)
##        else:
##            print("your pin is wrong")
##
##    def getter(self,a):
##        self.__display(a)
##
##obj = A()
##
##obj.set_pin(1236)
##
##obj.valid_pin(1234)
##
##obj.getter(1234)




##li = [1,3,4,5]



##from abc  import ABC,abstractmethod
##
##class Payment(ABC):
##
##    @abstractmethod
##    def pay(self,amt):
##        pass
##
##class cc(Payment):
##
##    def pay(self,amt,dis):
##        d1 = amt-(amt*dis/100)
##        print("after discount",d1)
##
##
##class paypal(Payment):
##
##    def pay(self,amt,tax):
##        d2 =  amt+(amt*tax/100)
##        print("After Tax",d2)
##
##class Upi(Payment):
##
##    def pay(self,amt):
##        print("UPI",amt)

##obj = cc()
##obj.pay(100,10)
##
##obj1 = paypal()
##obj1.pay(100,12)
##
##obj2 = Upi()
##obj2.pay(1200)


##li = [1,2,4,5,6]
##
##
##for i in range(1,len(li),1):
##    if i not in li:
##        print(i)
##
##print(li)

##li = [2,7,40,50]
##
##li2 = []
##for i in range(0,len(li),1):
##    for j in range(i+1,len(li),1):
##        if li[i]+li[j]==9:
##            li2.append(li[i])
##            li2.append(li[j])
##            
##
##
##print(li2)


##
##from abc import ABC,abstractmethod
##
##
##class Shape:
##
##    @abstractmethod
##    def area(self,l,w):
##        pass
##
##    @abstractmethod
##    def perimeter(self,l,w):
##        pass
##
##class rectriangle(Shape):
##
##    def area(self,l,w):
##        print(l*w)
##
##    def perimeter(self,l,w):
##        print(2*(l+w))
##
##
##obj = rectriangle()
##obj.area(10,20)
##obj.perimeter(20,40)


##
##from abc import ABC,abstractmethod
##
##class vehicle(ABC):
##
##    @abstractmethod
##    def start(self):
##        pass
##
##class Car(vehicle):
##
##    def start(self):
##        print("Tata Nexon")
##
##class Bike(vehicle):
##    
##    def start(self):
##        print("Bajaj palsur")
##
##
##obj = Car()
##obj.start()
##
##obj1 = Bike()
##obj1.start()





##from abc import ABC,abstractmethod
##
##
##class Employee(ABC):
##
##    @abstractmethod
##    def calculate_salary(self):
##        pass
##
##
##class Developer(Employee):
##
##    def calculate_salary(self,salary,bonus):
##        print(salary+bonus)
##
##class Manager(Employee):
##
##    def calculate_salary(self,salary,incentive):
##        print(salary+incentive)
##
##obj = Developer()
##obj.calculate_salary(29,30)
##
##
##obj1 = Manager()
##
##obj1.calculate_salary(2000,300)







##from abc import ABC,abstractmethod
##
##class BankAccount(ABC):
##
##    @abstractmethod
##    def deposit(self):
##        pass
##
##    @abstractmethod
##    def withdraw(self):
##        pass
##
##
##class Saving(BankAccount):
##
##    balance = 10000
##    def deposit(self,amt):
##        s = self.balance + amt
##
##        print("After deposit your balance is a:-",s)
##
##    def withdraw(self,amt):
##        if self.balance>500:
##            d = self.balance-amt
##            print("After withdraw the amount is a:-",d)
##
##        else:
##            print("your balance is not sufficinet")
##
##class CurrentAccount(BankAccount):
##
##    balance = 7000
##
##    def deposit(self,amt):
##        s = self.balance+amt
##        print("the a current account balance",s)
##
##    def withdraw(self,amt):
##        if self.balance>0:
##            self.balance-=amt
##
##        else:
##            print("your balance is a zero")
##
##
##obj = Saving()
##obj.deposit(200)
##obj.withdraw(300)
##
##
##obj2 = CurrentAccount()
##obj2.deposit(350)
##obj2.withdraw(300)

##from abc import ABC,abstractmethod
##
##
##class Payment(ABC):
##
##    @abstractmethod
##    def pay(self):
##        pass
##
##class cc(Payment):
##
##
##    def pay(self,total,dis):
##
##        s = total-(total*2/100)
##
##        print("after discount",s)
##
##
##class Paypal(Payment):
##
##    def pay(self,total,tax):
##
##        s = total+(total*10/100)
##
##        print("after the a tax:--",s)
##
##class Upi(Payment):
##
##    def pay(self,total):
##        print("the total paymnet",total)
##
##obj = cc()
##obj.pay(200,3)
##
##obj1 = Paypal()
##obj1.pay(100,10)
##
##obj2 = Upi()
##
##obj2.pay(200)
        
        

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
##class Dog(Animal):
##
##    def sound(self):
##        print("the dog sound is bark")
##
##    def move(self):
##        print("the dog is walk showly")
##
##class Bird(Animal):
##
##    def sound(self):
##        print("the bird is fly")
##
##    def move(self):
##        print("the bird is chirp")
##
##
##class Fish(Animal):
##
##    def sound(self):
##
##        print("fish is swim in the water")
##
##    def move(self):
##        print("the fish is bubbles is created")
##
##
##obj = Dog()
##obj.sound()
##obj.move()
##
##obj1 = Bird()
##obj1.sound()
##obj1.move()
##
##obj2 = Fish()
##obj2.sound()
##obj2.move()




##from abc import ABC,abstractmethod
##
##class Appliance(ABC):
##
##    @abstractmethod
##
##    def turn_on(self):
##        pass
##
##
##class TV(Appliance):
##
##    def turn_on(self):
##        print("the tv is turn on when we click the button")
##
##class Washingmachine(Appliance):
##
##    def turn_on(self):
##        print("the washing machine is button is turn on")
##
##class AirConditioner(Appliance):
##
##    def turn_on(self):
##        print("the airconditioner is on")
##
##
##obj1 = TV()
##obj1.turn_on()
##
##obj2 = Washingmachine()
##obj2.turn_on()
##
##obj3 = AirConditioner()
##obj3.turn_on()
##    


##
##from abc import ABC,abstractmethod
##
##
##class Charger(ABC):
##
##    @abstractmethod
##    def charge_device(self):
##        pass
##
##class PhoneCharger(Charger):
##
##    def charge_device(self):
##        print("the phone is charge very slow")
##
##class LaptopCharge(Charger):
##
##    def charge_device(self):
##        print("the laptop charge very  fast")
##
##class CameraCharge(Charger):
##
##    def charge_device(self):
##        print("camera is charge very fast")
##
##obj = PhoneCharger()
##obj.charge_device()
##
##obj1 = LaptopCharge()
##obj1.charge_device()
##
##obj2 = CameraCharge()
##obj2.charge_device()



##from abc import ABC,abstractmethod
##
##
##class Transort(ABC):
##
##    @abstractmethod
##    def book_ticket(self):
##        pass
##
##class Bus(Transort):
##
##    def book_ticket(self):
##        print("the bus ticket is very low")
##
##class Train(Transort):
##
##    def book_ticket(self):
##        print("the train ticket is very very low")
##
##class Flight(Transort):
##
##    def book_ticket(self):
##        print("the filght ticket is very highh...")
##
##obj1 = Bus()
##obj1.book_ticket()
##
##obj2 = Train()
##obj2.book_ticket()
##
##obj3 = Flight()
##
##obj3.book_ticket()


##from abc import ABC,abstractmethod
##
##class MediaPlayer(ABC):
##
##    @abstractmethod
##    def play(self):
##        pass
##
##    @abstractmethod
##    def pause(self):
##        pass
##
##    @abstractmethod
##    def end(self):
##        pass
##
##class VidioPlayer(MediaPlayer):
##
##    def play(self):
##        print("we play the old songs in vidioplayer")
##
##    def pause(self):
##        print("we use the pasue button for stop the vidio")
##
##    def end(self):
##        print("if vidio is complete i end itt")
##
##class AudioPlayer(MediaPlayer):
##
##    def play(self):
##        print("Audio is play")
##
##    def pause(self):
##        print("the audio is pause")
##
##    def end(self):
##        print("the a Audio is end")
##
##obj1 = VidioPlayer()
##obj1.play()
##obj1.pause()
##obj1.end()
##
##obj2 = AudioPlayer()
##obj2.play()
##obj2.pause()
##obj2.end()


##from abc import ABC,abstractmethod
##
##class Game(ABC):
##
##    @abstractmethod
##    def start(self):
##        pass
##
##    @abstractmethod
##    def play(self):
##        pass
##
##    @abstractmethod
##    def end():
##        pass
##    
##
##class Cricket(Game):
##
##    def start(self):
##        print("mostly the criket season is start on april to may")
##
##    def play(self):
##        print("there are total 22 people are play this game")
##
##    def end():
##        print("the end of the a season of cricket is very bad days of the cricket lovers")
##
##
##class Football(Game):
##
##    def start(self):
##
##        print("the football is a game we like but we don't play")
##
##    def play(self):
##        print("we play  the a football in 182 countrys but in india does not crazy like other countries")
##
##    def end():
##        print("because in over contry we most like to play the cricket")
##
##class Chess(Game):
##
##    def start(self):
##        print("the chess is start with two members only")
##
##    def play(self):
##        print("there are a this type of the people are play chess they like the a slient game")
##
##    def end():
##        print("the a end of chess if we killed the upostion king then we we the a match")
##
##obj1 = Cricket()
##obj1.start()
##obj1.play()
##Cricket.end()
##
##obj2 = Football()
##obj2.start()
##obj2.play()
##Football.end()
##
##obj3 = Chess()
##obj3.start()
##obj3.play()
##Chess.end()
##
##class A:
##
##
##    def __init__(self,a,b):
##        self.name = a
##        self.age = b
##
##
##    def __str__(self):
##        return f"the name :--{self.name} the age is a :--{self.age}"
##
##
##n = int(input("enter how many student you try to add"))
##li=[]
##for i in range(n):
##    a = A(input("enter the name:-"),input("enter the  age:-"))
##    li.append(a)
##
##
##for i in li:
##    print(i)



##class A:
##
##    def __init__(self,a,b):
##        self.name = a
##        self.age = b
##
##
##    def __str__(self):
##
##        return f"the name is :--{self.name} the age is a:-{self.age}"
##
##
##obj = A("roshan",21)
##
##obj1 = A("tushar",22)
##
##li = [obj,obj1]
##
##for i in li:
##    print(i)



##from abc import ABC,abstractmethod
##
##class Libraryitem(ABC):
##
##    @abstractmethod
##    def get_info(self):
##        pass
##
##    @abstractmethod
##    def borrow_item(self):
##        pass
##
##
##class Book(Libraryitem):
##
##    def get_info(self):
##        print("we have multiple book avilable in libarary")
##
##    def borrow_item(self):
##        print("we borrow the game of thorones book")
##
##class Magazine(Libraryitem):
##
##    def get_info(self):
##        print("the magazine are also avilable in pair of multiple")
##
##    def borrow_item(self):
##        print("the magazine is so expensive price")
##
##class DVD(Libraryitem):
##
##    def get_info(self):
##        print("the a DVD are avilable but in small amount")
##
##    def borrow_item(self):
##        print("you also borrow it but the a you have the perimium card for buy it:")
##
##obj1 = Book()
##obj1.get_info()
##obj1.borrow_item()
##
##obj2 = Magazine()
##obj2.get_info()
##obj2.borrow_item()
##
##
##obj3 = DVD()
##obj3.get_info()
##obj3.borrow_item()







##
##
##
##def m1():
##    print("hellow")
##
##
##m2 = m1
##
##del m1
##
##m2()

##
##
##
##
##
##def m1():
##
##    print("m1 is calling")
##
##    def m2():
##        print("m2 is calling")
##
##        def m3():
##            print("m3 is calling")
##
##            def m4():
##                print("m4 is calling")
##
##            return m4
##        return m3
##    return m2
##
##
##a = m1()
##
##b = a()
##
##c = b()
##
##d = c()

















##for i in range(5,0,-1):
##    print(" "*i,"*"*5)




##for i in range(0,5,1):
##    print(" "*(5-i),"*"*((2*i)-1))
##
##
##for i in range(4,1,-1):
##    print(" "*(6-i),"*"*((2*i)-3))
##    


##
##
##for i in range(0,5,1):
##    for j in range(0,5,1):
##        if i==0 or j==0 or i==4 or j==4:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##
##    print()




for i in range(0,5,1):
    print("*"*i)



























