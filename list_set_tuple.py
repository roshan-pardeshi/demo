
##
##li = [(1,2),(3,4),(1,2)]
##
##
##li = set(li)
##
##print(li)


##st = ["amit","rahul","priya","amit","neha","rahul"]
##
##st = set(st)
##
##print(st)
##
##
##st = tuple(st)
##
##print(type(st))
##
##print(sorted(st))
##

##li = [1,2,3,4,5,6]
##
##print(type(li))
##
##li = tuple(li)
##print(type(li))
##
##li = set(li)
##print(type(li))


##
##li = [10,20,30,40,50]
##
##li1 = (30,40,50,60)

##li = set(li)
##
##li1 = set(li1)
##
##
##print(li.intersection(li1))

##
##a = [1,2,3,4,5]
##
##b = (4,5,6,7,8)
##
##a = set(a)
##
##b = set(b)
##
##
##print(a.intersection(b))
##
##print(a.difference(b))
##
##
##print(b.difference(a))
##
##
##print(a.symmetric_difference(b))
##
##print(a.union(b))

##num = [10,20,30,40,50,10,20,30]
##
##num1=[]
##
##
##for i in range(len(num)):
##    if num[i] not in num1:
####        num1.append(num[i])
##        pass
##    else:
##        print(num[i])
##
##print(num1)
##




##
##li = [10,20,10,30,40,20,50]
##
##num = []
##for i in li:
##    if li.count(i)>1 and i not in num:
##        pass
##    else:
##        num.append(i)
##
##print(num)


##li = [10,20,30,40,50]
##
##li =set(li)
##
##tu = (30,40,50,60)
##
##tu = set(tu)
##
##se = {40,50,60}
##
##num = li.intersection(tu)
##
##print(num.intersection(se))


##li = []
##
##n = int(input("enter:-"))
##
##for i in range(0,n,1):
##    a = int(input("enter the number"))
##    li.append(a)
##
##
##for i in li:
##    
##
##word = ["python","java","python","sql","java","html","sql"]
##
####count = 0
##
##
####for i in word:
####    count+=1
####
####
####print(count)
##    
##
##word = set(word)
##
##print(word)
##
##
##print(sorted(word))
##
##stu = [("amit",85),
##       ("rahul",72),
##       ("roshan",90),
##       ("neha",75)
##       ]
##
##
##print(stu[0][0])
##
##
##for i in stu:
##    print(i[0])

##stu = [("amit",85),
##       ("rahul",72),
##       ("roshan",90),
##       ("neha",75)
##       ]
##
##for i in stu:
##    print(i[1]/4)


emp = [("amit","IT",50000),
       ("rahul","HR",60000),
       ("priya","IT",78000),
       ("Neha","sales",45000)
       ]
##
##for i in emp:
##    if i[1]=="IT":
##        print(i)
##
##for i in emp:
##    if i[2]>50000:
##        print(i)
####        
##
##for i in emp:
##    print(i[2]/4)
##    
##a = []
##
##for i in emp:
##    print(set(i[0]))


##
##li = [10,20,30,40,50,40,50]
##max1 = li[0]
##
##max2 = 0
##
##for i  in li:
##    if max1<i:
##        max1=i
##
##    if max1>i and max2<i:
##        max2=i
##
##
##print(max1)
##print(max2)

    
##
stu = {"amit":10,"roshan":20,"ravi":99,"sita":100,"neha":100}
##
##
##print(stu.keys())


##stu.update({"anikit":99})
##
##print(stu)


##stu["ravi"] = 80
##
##print(stu)

##
##stu.pop("neha")
##
##print(stu)


##for i in stu:
##    if i == "sita":
##        print("ahee re bhauu...")
##
##for i in range(len(stu)):
##        print(stu[i])


##d1 = "datasceince"
##d2 ={}
##
##for i in d1:
##    if i not in d2:
##        d2[i]=+1
##
##print(d2)

####d1 = {"a":1,"b":2}
####
####d2 = {"c":3,"d":4}
####
####
####d1.update(d2)
####
####print(d1)


##d1 = {"101":{"name":"amit","age":19,"marks":65},
##      "102":{"name":"manish","age":20,"marks":100}
##      }
##
##print(d1["101"])


##d1 = {1:1,2:2,3:3}
##val={}
##for i in d1:
##    val[d1[i]]=i**2
##
##
##print(val)

li = [1,2,3,4,5,6,7,8,9,10]

##res = list(map(lambda x:x**2,li))
##
##print(res)


##res = list(filter(lambda x:x%2==0,li))
##
##print(res)

##li = ["apple","banana","kiwi","pear"]
##
##res = list(filter(lambda x:len(x)>4,li))
##
##print(res)


##li = [0,20,37,100]
##
##res = list(map(lambda x:x+(9/5)+32,li))
##
##print(res)


##li = [12,15,20,22,29,30]
##
##res = list(filter(lambda x:x%5==0 and x%10!=0,li))
##
##print(res)



##li = ["python","java","c","ruby"]
##
##
##res = list(map(lambda x:len(x),li))
##
##print(res)


##tu = (10,20,30,40,50)
##
##res = tuple(map(lambda x:str(x),tu))
##
##print(res)


##tu = (10,20,30,40,50)
##
##res = tuple(filter(lambda x:x%3==0,li))
##
##print(res)

##tu = (1,2,-3,-4,5,-1)
##
##res = tuple(map(lambda x:x*(-1) if x<0 else x,tu))
##
##print(res)

##tu = (11,22,33,44,35,23,12)
##
##res = tuple(filter(lambda x:x%10==3,tu))
##
##print(res)


##
##se = {1,2,3,4,5,5,6}
##
##res = tuple(map(lambda x:x*2,se))
##
##print(res)

##se = {1,2,3,4,5,6,7,8,9}
##
##res = set(map(lambda x:x**0.5,se))
##
##print(res.2)


##se = {100,200,300,400,500,600,700}
##
##res = set(filter(lambda x:x>300,se))
##
##print(res)





##di = {"a":5,"b":12,"c":18,"d":3}
##
##res = dict(filter(lambda x:x[1]>10,di.items()))
##
##print(res)




##di = {"x":1,"y":2,"c":3}
##
##res = dict(map(lambda x:(x[0],x[1]**3),di.items()))
##
##print(res)

##
##di = {"apple":1,"cherry":2,"kiwi":3,"banana":4}
##
##res = dict(map(lambda x:(x[0].upper(),x[1]),di.items()))
##
##print(res)


##di = {"roshan":99,"tushar":109,"krishna":111,"pratik":1000}
##
##res = dict(filter(lambda x:x[1]>100,di.items()))
##
##print(res)


##pri = {"pen":10,"book":20,"pencil":100}
##
##res = dict(map(lambda x:(x[0],x[1]-(x[1]*10)/100),pri.items()))
##
##print(res)



##
##d1 = {}
##
##for i in range(0,5,1):
##    a = int(input("enter the name/others things"))
##    d1[i]=a
##
##
##print(d1)

##li = [1,2,3,4,5,1,2]
##li1=[]
##
##for i in li:
##    if li.count(i)>1 and i not in li1:
##        li1.append(i)
##
##
##print(li1[1])



##li =[100,200,300,400,100,100,1100]
##max2=[]
##
##max1 = li[0]
##max2=[]
##for i in li:
##    if max1<i:
##        max1=i
##        
##
##li.remove(max1)
##max2=li[0]
##for i in li:
##    if max2<i:
##        max2=i
##        
##
##    
######
##print(max2)
##
##
##


##file = open("text.txt","w")
##
##file.write("roshan\nsonu\nrohit\nmanish\nmohit")
##
##file.close()




##file = open("text.txt","r")
##
##            
##
##print(file.read())
##
##file.close()









##file = open("text.txt","r")
##
##data = file.readlines()
##count=0
##for i in data:
##    count+=1
##
##print(count)
##
##file.close()

##file = open("text.txt","r")
##
##data = file.readlines()
##
##for i in data:
##    print(i.strip())

##file = open("text.txt","a")
##
##file.write("vijay")
##
##file.close()
##
##file=open("text.txt","r")
##
##print(file.read())
##
##file.close()


##file = open("text2.txt","x")


##file = open("text.txt","r+")
##
##data=file.readlines()
##
##
##file1 = open("text2.txt","w")
##
##file1.writelines(data)
##
##file.close()
##file1.close()

##file = open("text2.txt","r")
##
##print(file.read())
##
##file.close()

##file = open("text2.txt","w")
##
##file.write("10\n20\n30\n40\n50")
##
##file.close()

##
##file = open("text2.txt","r")
##
##data = file.readlines()
##
##
##sum1 = 0
##
##for i in data:
##    sum1+=int(i)
##
##
##print(sum1)



##file = open("text.txt","w")
##
##file.write("roshan\nsonu\nrohit\nmanish\nmohit")
##
##file.close()

##
##file = open("text.txt","r")
##
##data = file.readlines()
##
##for i in data:
##    if i.startswith("r") or i.startswith("i") or i.startswith("o") or i.startswith("u"):
##        print(i)
####    else:
####        print(i.strip())
##
##
##file = open("text.txt","r")
##
##data = file.readlines()
##
##for i in data:
##    print(i.strip())

##
##li = [1,2,3,4,5,6,7,8,9,10]
##
##
##print(li[::-1])

##
##st = "roshan"
##
##li1 = "sonu"
##
##
##for i in range(0,len(st),1):
##
##    if st[i] in li1:
##        print(st[i])




##li = [1,2,3,4,5,6,7,8,9,10]
##
##
##for i in li:
##    if i%2==0:
##        print(i)
##
##li = [1,2,3,4,5,6,7,8,9,10]
##
##
##for i in li:
##
##    if i%3==0:
##        print("hazaa")
##    elif i%5==0:
##        print("fizaa")
##    else:
##        print(i)

##
##li  = [1,2,3,4,5,6,7,8,9,10]
##
##count =0
##for i in li:
##    if i%2==0:
##        count+=1
##    
##
##
##
##
##print(count)

##
##li = [1,2,3,4,5,6,6,6]
##
##
##print(max(li))
##
##print(min(li))
##
##print(li.count(1))
##
##li = [1,2,3,4,5,6,7,1]
##count = 0
##
##for i in range(0,len(li),1):
##    if li.count(i)>1:
##        count+=li[i]
##
##
##print(count)















##li = [1,2,3,4,5,6,7,1,2,3,4]
##
##li1 = []
##
##for i in range(0,len(li),1):
##    if li[i] in li1:
##        pass
##    else:
##        li1.append(li[i])
##
##
##print(li1)



##
##li = [10,20,40,300,1200,42,2001,1100]
##
##max1 = li[0]
##
##
##for i in li:
##    if max1<i:
##        max1=i
##        li.remove(max1)
##
##
##
##max2 = 0
##
##for i in li:
##    if max2<i:
##        max2 = i
##
##print(max2)


##tu = (10,20,30,10,10,40,50)
##
##print(tu.count(10))

##st = "aabbcdd"
##
##for i in range(0,len(st),1):
##    count = st.count(st[i])
##
##
##    if count==1:
##        print(st[i])
    
    
##st = "listen"
##st2 = "slient"
##
##for i in range(0,len(st),1):
##    if len(st)==len(st2):
##        if st[i] in st2:
##            print(st[i])


##
##li = [1,2,3,4,5,1,2]
##
##li1 = []
##
##for i in range(0,len(li),1):
##
##    if li.count(li[i])>1 and li[i] not in  li1:
##        li1.append(li[i])
##
##print(li1)
    

##li = [1,2,3,4,5,6,7,8,9]
##
##print(li[::-1])

##
##li = [1,0,2,0,4,5,6]
##
##count = 0
##li1=[]
##for i in range(0,len(li),1):
##
##    if li[i]==0:
##        count+=1
##    else:
##        li1.append(li[i])
##for i in range(count):
##    li1.append(0)
##print(li1)      


##li = [1,2,3,4]
##
##li1 = [1,2,4,5,7]
##
##li = set(li)
##li1 = set(li1)
##
##print(li.intersection(li1))
##


##word = ["roshan","sonu","pardeshi","sonumonu"]
##size = word[0]
##
##for i in word:
##    if len(i)>len(size):
##        size = i
##
##
##print(i)

##st = "python programming"
##
##count = 0
##
##for i in st:
##    if i=="a" or i=="e" or i=="o" or i=="u" or i=="i":
##        count+=1
##
##
##print(count)
    
##li = [1,2,3,4,5,6,5]
##
##re = 0
##
##for i in range(0,len(li),1):
##
##    if li.count(li[i])>1:
##        re=li[i]

##print(re)



##li = [1,2,3,4,5,6,7,8,9,10]
##
##li1 = []
##
##for i in range(0,len(li),1):
##    for j in range(i+1):
##        if i+j==10 and i>j:
##            li1.append(li[j])
##
##
##print(li1)


##
##words = ["python", "java", "python", "c", "java", "python"]
##
##
##for i in range(0,len(words),1):
##
##    count = words.count(words[i])
##
##    if count>2:
##        print(words[i])
##        break












