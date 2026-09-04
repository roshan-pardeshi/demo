

##try:
##    a = int(input("enter the first number"))
##    b = int(input("enter the second number"))
##
##    c = a/b
##
##except ZeroDivisionError:
##    print("zero division error occurs")
##else:
##    print(c)
##
##finally:
##    print("program excute succefully")

##
##try:
##    a = int(input("enter the number"))
##    b = int(input("enter the second number"))
##
##except ValueError:
##    print("invalid value you enter")
##
##else:
##    print(a,b)

##
##try:
##    a = int(input("enter the number"))
##    b = int(input("enter the second number"))
##
##    try:
##        c=a/b
##    except ZeroDivisionError:
##        print("zero division error occurs")
##except ValueError:
##    print("value error occurs")
##else:
##    print(a,b)


##try:
##    a = int(input("enter the number"))
##
##    b = int(input("enter the second number"))
##    c = a/b
##
##except Exception:
##    print("Error")
##
##else:
##    print(c)
##finally:
##    print("program are excute succefully")
##



##try:
##    a = int(input("enter the first number"))
##    b = int(input("enter the second number"))
##    c = a/b
##
##except (ValueError , ZeroDivisionError):
##    print("the error is occurs")
##else:
##    print(c)
##    
##finally:
##    print("the program is excute")
####    

##try:
##    a = int(input("enter the number"))
##    b= int(input("enter the number 2:-"))
##    c = a/b
##
##except Exception as e:
##    print(e)
##
##
##
##else:
##    print(c)
##
##
##class odd_number_error(Exception):
##    pass
##
##
##try:
##    age = int(input("enter the age:-"))
##
##    if age%2!=0:
##        raise odd_number_error
##
##except odd_number_error:
##    print("odd number you added")
##
##else:
##    print(age)

##
##class NagetiveNumberError(Exception):
##    pass
##
##try:
##    number = int(input("enter the number"))
##
##    if number<0:
##        raise NagetiveNumberError
##
##except NagetiveNumberError:
##    print("nagetive number")
##else:
##    print(number)
##


##li = [1,2,3,4,5]
##
##print(li[10])
##





##try:
##    st = "abcd"
##
##    st.append(st)
##    
##except AttributeError:
##    print("give input is string")
##else:
##    print(st)


##try:
##    a= int(input("enter the number"))
##
##    b = int(input("enter the second number"))
##
##    c = a/b
##
##except ZeroDivisionError:
##    print("error occurs")
##
##else:
##    print(c)

##
##
##try:
##    a = int(input("enter the number"))
##    b = int(input("enter the second number"))
##
##    c = a/b
##
##except Exception as e:
##    print("error is a",e)
##
##else:
##    print(c)





##def factorial(n):

##fact = 1######sds

##    for i in range(1,n+1,1):
##        fact = fact*i
##
##    return fact
##num = 14
##
##sum1=0
##
##for i in str(num):
##    sum1+=factorial(int(i))
##
##if sum1==num:
##    print("strong number")
##
##else:
##    print("not a strong number")



##
##try:
##    a = int(input("enter the number:-1:-"))
##    b = int(input("enter the second number 2:-"))
##    c = a/b
##
##except ZeroDivisionError:
##    print("error are occurs during exution")
##
##else:
##    print(c)


##try:
##    a = int(input("enter 1:-"))
##    b = int(input("enter 2:-"))
##
##except ValueError:
##    print("value error are created")
##else:
##    print(a+b)

##
##try:
##    li=[1,2,3,4,5]
##
##    print(li[10])
##
##except IndexError:
##    print("index error")
##    
##else:
##    print(li)
##
##finally:
##    print("program excuted")

##
##try:
##    a = int(input("enter 1:-"))
##    b = int(input("enter 2:-"))
##    c = a/b
##
##except ValueError ,ZeroDivisionError:
##    print("error are occurs")
##
####else:
####    print("c",c)
##
##          
##
##try:
##    a = int(input("enter the number"))
##
##    fact = 1
##
##    for i in range(1,a+1,1):
##        fact*=i
##
##
##except ValueError:
##    print("input is not a integer")
##
##else:
##    print(fact)
##


##try:
##
##    d1 = {1:"roshan",
##          2:"sonu",
##          3:"saurbh",
##          4:"pratik"
##          }
##
##    print(d1[6])
##
##except KeyError:
##    print("key is not present")
##
##else:
##    print(d1)

##
##try:
##    st = "abcdefghijknmpqrswxyz"
##
##    st.append("sonu")
##
##except AttributeError:
##    print("not used for string")
##
##else:
##    print(st)


##try:
##    a = "roshan"
##
##    print(c)
##
##except NameError:
##    print("the variable are not present ")
##
##else:
##    print(a)
##

##
##try:
##    a = int(input("enter 1:="))
##    b = int(input("enter 2:="))
##
##    c = a/b
##
##except ZeroDivisionError:
##    print("division not possiable")
##
##
##else:
##    print(c)

##
##
##try:
##    a = int(input("enter the number 1:-"))
##
##    b = int(input("enter the number 2:-"))
##
##    c = a/b
##
##except Exception:
##    print("error  occurs")
##
##else:
##    print(c)


##try:
##    a = 100
##    b= 0
##
##    c = a/b
##
##except ValueError,ZeroDivisionError:
##    print("error ahe bhauu...!!!!!")
##
##else:
##    print(c)



##
##try:
##
##    a = "roshan1"
##
##    print(a.upper())
##
##    b = 10
##
##    c = 20
##
##    d = 0
##
####    e = c/d
##
##    li = [1,2,3,4,5]
##
##    print(li.count(20))
##
##   
##except Exception  as e:
##    print("hii",e)
##
##else:
##    print("e")


##
##try:
##    a = int(input("enter 1:"))
##    b = int(input("enter 2:"))
##
##    try:
##        c = a+b
##        print(c)
##        
##    except ValueError:
##        print("value error")
##        
##
##    d = a/b
##
##except ZeroDivisionError:
##    print("ZeroDivision Error")
##
##    
##
##finally:
##    print("calculation Finished")
##



##class NegativeError(Exception):
##    pass
##
##
##try:
##    age = int(input("enter the age"))
##
##    if age<0:
##        raise NegativeError
##
##except NegativeError:
##    print("its -ve")
##
##else:
##    print(age)

##
##class SmallStringError(Exception):
##    pass
##
##
##try:
##    st = "rosn"
##
##    if len(st)<5:
##        raise SmallStringError
##
##except SmallStringError:
##    print("small string")
##
##else:
##
##    print(st)
##    




##class EvenNumberError(Exception):
##    pass
##
##
##try:
##    num = int(input("enter the number"))
##
##    if num%2==0:
##        raise EvenNumberError
##
##
##except EvenNumberError:
##    print("not used the even number")
##
##
##else:
##    print(num)
##

##
##class AgeValidationError(Exception):
##    pass
##
##
##try:
##    age = int(input("enter your age"))
##
##    if age<18 or age>100:
##        raise AgeValidationError
##
##
##except AgeValidationError:
##    print("this an error")
##
##else:
##    print(age)

##
##
##class PasswordValidationError(Exception):
##    pass
##
##
##try:
##    pass_word = input("enter your password")
##
##    if len(pass_word)>=8  and pass_word.isalnum():
##        pass
##    else:
##        raise PasswordValidationError
##
##except PasswordValidationError:
##    print("hello")
##
##else:
##    print(pass_word)
##        


##class InvalidRollNumberError(Exception):
##    pass
##
##
##try:
##    roll_no = int(input("enter the rollnumber"))
##
##
##    di = {1:"roshan",2:"sonu",3:"rohit"}
##    print(di)
##
##    d = di.keys()
##
##    if roll_no in d:
##        print(d)
##    else:
##        raise InvalidRollNumberError
##
##    
##
##except InvalidRollNumberError:
##    print("in valid rollnumber")


##
##class OutofStockError(Exception):
##    pass
##
##try:
##    onion = 100
##    chily = 50
##    while True:
##        print("1.onion\n2.chily")
##        user = int(input("enter the quantity"))
##        choice = int(input("enter choice"))
##        match(choice):
##            case 1:
##                onion-=user
##                if onion<0:
##                    raise OutofStockError
##                
##        
##except OutofStockError:
##    print("the item is Out of stock")
##
##
##except Exception:
##    print("hi")


##print(type(onion))
##
##
##class ZeroInputError(Exception):
##    pass
##
##try:
##    a = int(input("enter the number"))
##
##
##    if a<=0:
##        raise ZeroInputError
##
##except ZeroInputError:
##    print("ahe error bhau!!")
##
##else:
##    print(a)
##    


##
##class EmptyStringError(Exception):
##    pass
##
##try:
##    st = input("enter the string")
##
##    if len(st)==0:
##        raise EmptyStringError
##
##except EmptyStringError:
##    print("its and error occurs")
##
##else:
##    print(st)
##



##
##class DivisionByNegativeError(Exception):
##    pass
##
##try:
##    a = int(input("enter the number:-"))
##
##    b = int(input("enter the number:-"))
##
####    c = a/b
##
##    if a%2==0 and b%2==0:
##        raise DivisionByNegativeError
##
##
##except DivisionByNegativeError:
##    print("hii")
##
##
##
##else:
##    print(a)
##    print(b)

##
##class ShortNameError(Exception):
##    pass
##
##
##try:
##    st = "ro"
##
##    if len(st)<3:
##        raise ShortNameError
##
##except ShortNameError:
##    print("its short length")
##
##else:
##    print(st)



##
##class OddNumberError(Exception):
##    pass
##
##try:
##    a = int(input("enter the number"))
##
##    if a%2!=0:
##        raise OddNumberError
##
##except OddNumberError:
##    print("its odd number")
##
##else:
##    print(a)


class MarksOutOfRangeError(Exception):
    pass


try:
    student_marks = int(input("enter the marks"))


    if student_marks<0 or student_marks>100:
        raise MarksOutOfRangeError


except MarksOutOfRangeError:
    print("marks out of range")

else:
    print(student_marks)





































































































































































































    





































