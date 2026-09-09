
##
##class A:
##
##    def show(self):
##        print("public method")
##
##    def _show(self):
##        print("protected method")
##
##
##    def __show(self):
##        print("private method")
##
##    def getter(self):
##        self.__show()
##
##a = A()
##
##a.show()
##a._show()
##a.getter()
        












##from abc import ABC,abstractmethod
##
##
##class A(ABC):
##
##    def show(self):
##        pass
##
##class B(A):
##    def show(self):
##        print("abstract method")
##
##o = B()
##
##o.show()


##
##from abc import ABC,abstractmethod
##
##
##class A:
##
##    def display(self):
##        pass
##
##class B(A):
##
##    def display(self):
##        print("abstract method")
##
##a = B()
##a.display()

##
##from abc import ABC,abstractmethod
##
##
##class Shape(ABC):
##
##    @abstractmethod
##    def area(self):
##        pass
##    @abstractmethod
##    def peimeter(self):
##        pass
##
##
##class rectriangle(Shape):
##    l= 10
##    w = 20
##
##
##    def area(self):
##        print("area of rectriangle",self.l*self.w)
##
##    def peimeter(self):
##        print("peimeter:-",2*(self.l+self.w))
##
####class Circle(Shape):
####    l = 10
####    w = 30
####
####    def peimeter(self):
####        print("peimeter:-",2*(self.l+self.w))
####
##o = rectriangle()
##
##o.area()
##o.peimeter()

##c = Circle()
##
##c.peimeter()




##from abc import ABC,abstractmethod
##
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
##        print("car is start")
##
##
##class bike(vehicle):
##
##    def start(self):
##        print("bikce is start")
##
##
##a = Car()
##a.start()
##
##b = bike()
##b.start()

from abc import ABC,abstractmethod
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
##    salary_developer = int(input("enter the developer salary:--"))
##
##    bonus = int(input("enter the bonus of the developer:--"))
##
##    def calculate_salary(self):
##        print(self.salary_developer+self.bonus)
##
##class Manager(Employee):
##
##    salary = int(input("enter the salary:--"))
##
##    incentive = int(input("enter the incentive:--"))
##
##    def calculate_salary(self):
##        print(self.salary+self.incentive)
##
##a = Developer()
##
##a.calculate_salary()
##
##b = Manager()
##
##b.calculate_salary()

    

##class BankAccount(ABC):
##
##    balance = 10000
##    @abstractmethod
##    def deposit(self):
##        pass
##
##    @abstractmethod
##    def withdraw(self):
##        pass
##
##class SavingAccount(BankAccount):
##
##    def deposit(self,v1):
##
##        s = self.balance+self.v1
##        print("after deposit",s)
##
##    def withdraw(self,v2):
##        if self.balance>500:
##            b = self.balance-self.v2
##
##
##class CurrentAccount(BankAccount):
##
##    def deposit(self,v3):
##        s = self.balance + self.v3
##
##
##    def withdraw(self,v4):
##        if self.balance>500:
##            b = self.balance-self.v4
##
##
##
##a = SavingAccount()
##
##a.deposit(2000)
##
##a.withdraw(300)
##
##c = CurrentAccount()
##
##c.deposit(400)
##
##c.withdraw(4000)


##from abc import ABC,abstractmethod
##
##
##class Shape(ABC):
##
##    @abstractmethod
##    def area(self):
##        pass
##    @abstractmethod
##    def peimeter(self):
##        pass
##
##
##class rectriangle(Shape):
##
##    l = 20
##    w = 30
##
##    def area(self):
##        print(self.l*self.w)
##
##    def peimeter(self):
##        print(2*(self.l+self.w))
##
##a = rectriangle()
##
##a.area()
##
##
####a.peimeter()
##
##
##from abc import ABC,abstractmethod
##
##
##class Vehicle(ABC):
##
##    @abstractmethod
##    def start(self):
##        pass
##
##class Car(Vehicle):
##
##    def start(self):
##        print("this is a class of car")
##
##
##class Bike(Vehicle):
##
##    def start(self):
##
##        print("this is a Bike class")
##
##
##a = Car()
##a.start()
##
##b = Bike()
##b.start()


##from abc import ABC,abstractmethod
##
##
##class Employee(ABC):
##
##    @abstractmethod
##    def calculate_salary(self):
##        pass
##
##class Developer(Employee):
##
##
##    salary = 10000
##    bonus = 23
##    def calculate_salary(self):
##        s = self.salary+self.bonus
##        print(s)
##
##class Manager(Employee):
##
##    salary = 2000
##    incentive = 15
##
##    def calculate_salary(self):
##        print(self.salary+self.incentive)
##
##
##a = Developer()
##a.calculate_salary()
##        
##b = Manager()
##b.calculate_salary()

        
##from abc import ABC,abstractmethod
##
##
##class BankAccount(ABC):
##
##   
##
##    @abstractmethod
##
##    def deposit(self):
##        pass
##
##    @abstractmethod
##    def withdraw(self):
##        pass
##
##
##class SavingAccount(BankAccount):
##    balance = 10000
##    deposit_amount = 1000
##    withdraw_amount = 500
##        
##    def deposit(self):
##        s = self.balance + self.deposit_amount
##        print(s)
##
##    def withdraw(self):
##        if self.balance>500:
##            d = self.balance - self.withdraw_amount
##            print(d)
##
##try:
##    class CurrentAccount(BankAccount):
##
##        def deposit(self):
##            print("is an a deposit section of the a Current Account",self.deposit)
##
##        def withdraw(self):
##            pass
##            
##except Exception:
##    print("is an error")
##
##
##a= SavingAccount()
##a.deposit()
##a.withdraw()
##
##b = CurrentAccount()
##b.deposit()
##b.withdraw()






##from abc import ABC,abstractmethod

##
##class Payment(ABC):
##    @abstractmethod
##    def Pay(self):
##        pass
##
##
##class CreditCardPayment(Payment):
##
##    def Pay(self):
##        print("the self of the amount using--creadit card payment")
##
##class Payment2(Payment):
##
##    def Pay(self):
##        print("the self of the a amount using:---payment2")
##
##
##a = CreditCardPayment()
##a.Pay()
##
##b = Payment2()
##b.Pay()


from abc import ABC,abstractmethod

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
##        print("the dog is like bark_bark")
##
##    def move(self):
##        print("the movement like a walk")
##
##class Bird(Animal):
##
##    def sound(self):
##        print("the bird is fly in the sky")
##
##    def move(self):
##        print("the a bird is a chirp in the sky")
##        
##
##class Fish(Animal):
##
##    def sound(self):
##        print("the fish is run in the water")
##
##    def move(self):
##        print("the a fish movement is like air is tevels thoron the a gap")
##
##
##d = Dog()
##d.sound()
##d.move()
##
##b = Bird()
##b.sound()
##b.move()
##
##f = Fish()
##f.sound()
##f.move()
##    
    


##from abc import ABC,abstractmethod
##
##
##class Appliance(ABC):
##    
##    @abstractmethod
##    def method_turn(self):
##        pass
##
##class TV(Appliance):
##
##    def method_turn(self):
##        print("the tv is turn on when we press the button")
##
##class washing_machine(Appliance):
##
##    def method_turn(self):
##        print("if we try to wash over clocks we turn on the washing machine")
##
##class moblie(Appliance):
##
##    def method_turn(self):
##        print("if we press the button of the mobile phone the phone is turn on")
##
##a = TV()
##a.method_turn()
##
##b = washing_machine()
##b.method_turn()
##
##c = moblie()
##c.method_turn()
    
    

##from abc import ABC,abstractmethod
##
##
##class Charger(ABC):
##
##    @abstractmethod
##    def charge_device(self):
##        pass
##
##
##class Moblie_charger(Charger):
##
##    def charge_device(self):
##        print("we use the charger to charge the mobile phone less voltage charger like 100v or 120v")
##
##class Laptop(Charger):
##
##    def charge_device(self):
##
##        print("we use to charge the laptop using lager capacitiy charger like 150v to 200v")
##
##a = Moblie_charger()
##a.charge_device()
##
##b = Laptop()
##b.charge_device()
##



##from abc import ABC,abstractmethod
##
##class Transport(ABC):
##
##    @abstractmethod
##    def book_ticket(self):
##
##        pass
##
##
##class Bus(Transport):
##
##    def book_ticket(self):
##
##        print("in PMPML is pune buse servies to help student to tevels on location to ohter")
##
##class train(Transport):
##
##    def book_ticket(self):
##
##        print("in pune i remainber the metro services are best . of other word beacuse is upfortable") 
##
##class Airoplane(Transport):
##
##    def book_ticket(self):
##        print("the airoplane ticket is not afotable for every one beacuse is more expensive")
##
##a = Bus()
##a.book_ticket()
##
##b = train()
##b.book_ticket()
##
##c = Airoplane()
##c.book_ticket()


##from abc import ABC,abstractmethod
##
##class Media_Player(ABC):
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
##    def stop(self):
##        pass
##
##class Audio_player(Media_Player):
##
##    def play(self):
##
##        print("i really enjoy to lisen the raj shamani podcast")
##
##    def pause(self):
##
##        print("every 10 min letter i pause the podcast and a understand what his actully say")
##
##
##    def stop(self):
##
##        print("If i thing that the a padcast is so boring i try to stop it quaclly")
##
##class Vidio_Player(Media_Player):
##
##    def play(self):
##        print("i used to pass my time to lisen the a podcast")
##
##    def pause(self):
##        print("pause is importent thing i notice that same people is stop himself to try new word means his give the samll pasue before talk the sentance")
##        
##    def stop(self):
##        print("i stop the Vidio player beacuse his play very boring song")
##
##a = Audio_player()
##a.play()
##a.pause()
##a.stop()
##
##
##c = Vidio_Player()
##c.play()
##c.pause()
##c.stop()



##from abc import ABC,abstractmethod
##
##
##class Game(ABC):
##
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
##    def end(self):
##        pass
##
##
##class Cricket(Game):
##
##    def start(self):
##        print("I start the playing cricket in 2017 i am play with my friends in jaymahlar ground")
##
##    def play(self):
##        print("we divide the group of the boys i 6*6 beacuse in over group the member is very less")
##
##    def end(self):
##        print("every sunday we gone to ground at a 9 am and back to home 2 pm")
##
##class Football(Game):
##
##    def start(self):
##        print("we don't play the football but i seen the people to play the foot ball")
##
##    def play(self):
##
##        print("there are 11 player in each team to play the football")
##
##    def end(self):
##        print("every sunday start the a game at 3 am")
##
##class Chess(Game):
##
##    def start(self):
##
##        print("i really enjoy the play the Chess")
##
##    def play(self):
##        print("i miss my chess board beacuse every sunday i play the chess with my family")
##
##    def end(self):
##        print("every story end with the a best thing and best memeries to collect in your life")
##
##
##a = Cricket()
##a.start()
##a.play()
##a.end()
##
##b = Football()
##b.start()
##b.play()
##b.end()
##
##
##c = Chess()
##c.start()
##c.play()
##c.end()



##from abc import ABC,abstractmethod
##
##
##class Librayitem(ABC):
##
##    @abstractmethod
##    def get_info(self):
##        pass
##
##    @abstractmethod
##    def borrow_item(self):
##        pass
##
##class Book(Librayitem):
##
##    def get_info(self):
##        print("there are multiple book in library")
##
##    def borrow_item(self):
##        print("we borrow the book game of thornes")
##
##class Magazine(Librayitem):
##
##    def get_info(self):
##        print("i did't understand what they did")
##
##    def borrow_item(self):
##
##        print("borraw the book ")
##
##a = Book()
##a.get_info()
##a.borrow_item()
##
##b = Magazine()
##b.get_info()
##b.borrow_item()












        
    














































