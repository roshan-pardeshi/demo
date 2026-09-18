


##li = [1,2,3,4,5,6,7,8,9,10]


##for i in range(0,5,1):
##    a = int(input("enter the a number:-"))
##
##    li.append(a)

##
##print(li)
##
##li.insert(2,15)
##
##print(li)


##li.extend([11,12,13,14])
##
##print(li)
##
##li = ["apple","kiwi","banana","cherry","apple"]
##
##li.remove("apple")
##
##print(li)
##
##li.pop()
##
##print(li)

####li.clear()
##a = li.copy()
##print(a)

##print(li.index(7,1,7))


##print(li.count(2))


li = [9,7,6,5,4,4,3,1,2,3,1]
####
####
####print(sorted(li))
##
##li.sort(reverse=True)
##
##print(li[1])



##for i in range(len(li)-1,-1,-1):
##    print(li[i])
##



##colors = ["red","green","blue","yellow"]
##
##
####s = colors.copy()
####
####print(s)
##
##
##colors.remove("green")
##
##print(colors)



##s1 = [[1,2],[3,4],[5,6]]
##
####print(s1[1][1])
##
##
##s1.append([7,8])
##
##print(s1)



##s1.extend([[10,11],[12,13]])
##
##print(s1)

##
##
##li = [1,2,3,4,5,5,6,7,8,9,0]
####
####
####a = li[::-1]
####
####print(a[1])
##
##print(min(li))
##
##print(max(li))
##
##print(len(li))


##
##count =0
##
##li = [1,2,3,4,5,6,7,8,9,10]
##
##for i in li:
##    count+=1
##
##
##print("count of the list:--",count)
##
##print(li[0:5])
##
##
##print(li[:-1:-5])


li = [10,20,30,40,50]

##li.insert(2,25)
##
##print(li)
##
##
##li.remove(40)
##
##print(li)

##li.pop()
##li.append(100)

##li.replace(50,100)
##
##print(li)
##
##
##li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
##
##sum1 = 0
##
##for i in li:
##    if i%2==0:
##        print(i)
##    else:
##        sum1+=i
##
##print("addition:--",sum1)

        

##words = ["apple","banana","cherry","kiwi","mango"]
##
##for i in words:
##    if len(i)>5:
##        print(i.capitalize())
##


li = [    [1,2,3],
          
          [4,5,6],
          
          [7,8,9]
     ]

##
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        if i==j:
##            print(li[i][j])
##sum1 = 0
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        if i+j==2:
##            sum1+=li[i][j]
##                   
##print(sum1)
##
##
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        print(li[i][j])
##        
##    
##li =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
##
##for i in li:
##    if i % 2 == 0:
##        print(i)
##
##
##li = [1,23,11,3,14,1,3,2,13,13,14,122,144,1,13,1,3,4,1]
##
##
##li1 = []
##
##for i in range(0,len(li),1):
##    if li[i] in li1:
##        pass
##    else:
##        li1.append(i)
##
##print(li1)


##
##li = [12,13,4,11111,222,1333,134442,2,42444,1323,45000]
##
##
##a = sorted(li)
##
##print(a[-2])


##print(li[::-1])



##li = [1,2,3]
##
##li1 = ["a","b","c"]
##
##
##for i in range(0,len(li),1):
##    for j in li1:
##        li.append(j)
##        break
##
##
##print(li)



##
##li = [1,2,3]
##
##li2 = ["a","b","c"]
##li3=[]
##for i in range(0,len(li),1):
##    for j in range(len(li2)):
##        if li2[j] in li3:
##            pass
##        else:
##            li3.append(((li[i],li2[j])))
##            print(li2[j])
##            
##            
##            
##
##print(li3)
            

##
tu = (1,2,3,4,5,6,7,7,8,9,10)
##
##
##print(tu)
##
##print(tu[2])
##
##print(tu[::-1])

##tu = (1,2,3)
##tu2 = (5,6,7)
##
##tu3 = tu+tu2
##
##print(tu3)


##tu = ("HI",)
##
##print(tu*5)


##for i in tu:
##    if i==5:
##        print("ahe")

##count = 0
##
##for i in tu:
##    count+=1
##
####print(count)
##
##
##li = [1,2,3,4,5,6]
##
##li1 = tuple(li)
##
##print(type(li1))
##
##print(li1)

##tu = (10,20,30,40,50,60)
##
##tu1 = list(tu)
##
##print(tu1)
##
##print(type(tu))


##tu = (10,20,30,40,50)
####
####print(tu.index(20,0,4))
##
##print(min(tu))
##
##print(max(tu))
##
##tu = (1,2,3,(4,5),(6,7,(8,9)))
##
##print(tu[4][2][1])


##tu = (1,2,3)
##
##a = tu
##
##tu1 = (3,4,5)
##
##tu = tu1
##
##tu1=a
##
##
##
##
##print(tu)
##print(tu1)




##tu = ()
##
##print(type(tu))



##tu = (5,)
##
##print(type(tu))

##tu = (10,20,30,40)
##
##print(tu[-1])

##tu = (1,2,3,4,5,6,7)
##
##print(tu[1:4])


##
##class BankAccount:
##
##    def __init__(self,account_no,hod,amount):
##        self.a = account_no
##        self.b = hod
##        self.c = amount
##
##
##    def __str__(self):
##
##        return f" the account no:{self.a} the hod is :-{self.b} the a amount is :{self.c}"
##
##a = BankAccount("1234","roshan",2000)
##
##
##b = BankAccount("3244","tushar",22334)
##
##li = [a,b]
##
##for i in li:
##    print(i)























