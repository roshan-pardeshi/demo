##
##name = "roshan"
##
##age = 21
##
##print(f"name:-{name}the age is a:{age}")
##
##print("the name is a {} the age is a {}".format(name,age))

##a = input("enter the number")
##
##print(a)

##a = 4
##
##if a%2==0:
##    print("even number")
##
##else:
##    print("odd number")

##a = 1
##
##if a>0:
##    print("+ve number")
##elif a==0:
##    print("the number is a zero")
##else:
##    print("the -ve number")

##a = 10
##
##b = 20
##
##a = a^b
##b = a^b
##a = a^b
##
##print(a)
##print(b)

##
##for i in range(1,11):
##    print(i)

##
##i = 1
##while i<10:
##    print(i)
##    i+=1
    

##class A:
##
##    def show(self):
##        print("hello")
##
##obj = A()
##obj.show()


##li = [1,2,3,4,5,6]
##
##li.append(11)
##
##print(li)
##
##li.insert(1,123)
##
##print(li)
##
##li.extend([12,3,4,4])
##
##print(li)
##
##li.remove(11)
##
##print(li)
##
##li.pop()
##
##print(li)
##
##
##print(li.count(1))
##
##print(li.index(1,0,5))
##
##
##
##print(sorted(li))
##
##print(min(li))
##
##print(max(li))
##
##
##li1 = li.copy()
##
##print(li1)
##
##li.clear()
##print(li)


##
##tu = (1,2,3,4,5,6,7)
##
##
##print(tu.count(1))
##
##
##print(tu.index(2,0,4))
##
##
##print(min(tu))
##
##print(max(tu))
##
##print(len(tu))
##
##for i in tu:
##    print(i)

##
##se = {1,2,3,4,5,6,7,8,9,10}
##
##se1 = {1,2,3,4,8,9,14,15,16}
##
##
##print(se.union(se1))
##
##print(se.intersection(se1))
##
##print(se.difference(se1))
##
##print(se.symmetric_difference(se1))


##se.update({12,13,14})
##
##print(se)

##se.pop()
##
##print(se)
##
##print(sorted(se))

##
##d1 = {1:2,2:4,3:4,4:5}
##
##
##print(d1.keys())
##
##print(d1.values())
##
##d1.popitem()
##
##print(d1.items())
##
##
##d1.pop(1)
##
##print(d1)



##a = [1,2,3,4,5,6]
##
##res = list(map(lambda x:x*2,a))
##print(res)
##
##res1 = list(filter(lambda x:x%2==0,a))
##
##print(res1)
##
##
##
##a = {1,2,3,4,5,6,7}
##
##res = set(map(lambda x:x**3,a))
##print(res)
##
##res1 = set(filter(lambda x:x%2!=0,a))
##print(res1)
##
##
##
##
####
####
##a = {"roshan":1,"sonu":2,"rohit":4,"manish":5,"tushar":8}
##
##res = dict(map(lambda x:(x[0],x[1]**3),a.items()))
##
##print(res)
##
##
##
##res1 = dict(filter(lambda x:x[1]%2==0,a.items()))
##
##print(res1)


##class A:
##
##    def __init__(self,name):
##        self.name = name
##
##
##    def __str__(self):
##
##        return f"the name {self.name}"
##
##obj = A("roshan")
##
##
##print(obj)


##
##count = 0
##
##li = [1,2,3,4]
##
##for i in li:
##    count+=1
##
##print(count)
##
##
##li = [1,2,3,4,1,2,4,1]
##
##li1 = []
##
##for i in li:
##
##    if i not in li1:
##        li1.append(i)
##
##print(li1)


##st = "ababceerrrsss"
##
##
##for i in range(0,len(st),1):
##
##    count = st.count(st[i])
##
##    if count==1:
##        print(st[i])
    


##st = "roshan vijay pardeshi"
##
##st = st.split()
##
##size = st[0]
##
##for i in range(0,len(st),1):
##
##    if len(st[i])>len(size):
##        size = st[i]
##
##
##print(size)
    


##
li = [1,2,3,4,11,22,33,2,1]
##max1 = li[0] 
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
####
####print(max2)
##res = []
##for i in li:
##    if li.count(i)>1 and i not in res:
##        res.append(i)
##
##print(i)



3
##

##file = open("python.txt","w")
##
##file.write("roshan")
##
##file.close()





















