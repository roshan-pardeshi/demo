


##d1 = {}
##
##n = 5
##
##for i in range(n):
##    a = int(input("enter the number:-"))
##    d1[i]=a**2
##
##
##print(d1)


##
##li  =[[2,3,1],[3,2,5],[1,2]]
##
##sum1 = []
##
##
##for i in li:
##    sum1.append(sum(i))
##        
##a = sorted(sum1)
##
##print(a[-1])


##
##li = [1,2,3,4,1,2,3,4,5,6,6,7,7]
##
##for i in li:
##    count = li.count(i)
##
##    if count==1:
##        print(i)


##
##li = [10, 5, 8, 20, 15, 20, 3]
##
##li1 = []
##
##for i in li:
##    if i not in li1:
##        li1.append(i)
##
##    
##max1 = li1[0]
##
##for i in li1:
##    if max1<i:
##        max1=i
##
##li1.remove(max1)
##
##max2=li1[0]
##
##
##for i in li1:
##    if max2<i:
##        max2=i
##
##print(max2)
    

##words = ["python", "java", "programming", "code", "developer"]
##
##
##size = ""
##
##for i in words:
##    if len(i)>len(size):
##        size=i
##
##print(size)



##li = [1, 2, 3, 2, 4, 1, 5, 3, 6]
##
##re = []
##
##for i in li:
##    if li.count(i)>1 and i not in re:
##        re.append(i)
##
##print(re)

##
##li = [1, 2, 3, 5, 6, 7, 8]
##
##
##for i in range(1,len(li),1):
##    if i not in li:
##        print(i)


##li = [1, 2, 3, 4,5, 6, 7, 8,10,12,13]
##
##for i in range(1, len(li) + 2):
##    if i not in li:
##        print(i)


##li = [1, 2, 3, 4, 5, 6]
##li1 = [4, 5, 6, 7, 8, 9]
##
##li3 = []
##for i in range(0,len(li),1):
##    if li[i] in li1:
##        li3.append(li[i])
##
##print(li3)
        

##li = [1, 2, 2, 3, 1, 4, 2, 3, 5]
##
##
##
##
##for i in li:
##    count = li.count(i)
##
##    print(i," : ",count)



##li = [5, 3, 8, 2, 3, 9, 8]
##
##for i in li:
##    count = li.count(i)
##
##    if count>1:
##        print(i)
##        break


##li = [10, 20, 30, 40, 50]
##
##
##for i in range(len(li)-1,-1,-1):
##    print(li[i],end=" ")



##li = [1, 2, 3, 4, 5, 6, 7, 8]
##
##
##li1 = []
##li2 = []
##
##for i in li:
##    if i%2==0:
##        li1.append(i)
##    else:
##        li2.append(i)
##
##print("even:-",li1)
##
##print("odd:-",li2)


##li = [12, 5, 8, 21, 16, 7, 30, 11]
##
##sum_even =  0
##
##sum_odd = 0
##
##
##for i in li:
##    if i%2==0:
##        sum_even+=i
##    else:
##        sum_odd+=i
##
##print(sum_even)
##
##print(sum_odd)


##
##li = [10, 25, 7, 40, 15, 30, 5]
##
##max1 = li[0]
##
##for i in li:
##    if max1<i:
##        max1=i
##
##
##max2 = li[0]
##
##for i in li:
##    if max2>i:
##        max2=i
##
##
##count = 0
##
##for i in range(max2,max1,1):
##    count+=1
##
##
##print(count)
##li = [4, 7, 2, 9, 4, 7, 1, 9, 2]
##
##
##li1 = []
##
##for i in li:
##    if i not in li1:
##        li1.append(i)
##
##print(li1)


##li = [10, 20, 30, 40, 50]
##
##li1 = li[-1]
##
##li.pop()
##
##
##li.insert(0,li1)
##
##print(li)


##li = [2, 4, 6, 8, 10]
##
##
##
##li1  = []
##
##for i in li:
##    li1.append(i*2)
##
##
##print(li1)
##

##li = [12, 5, 8, 21, 16, 7, 30, 11]
##
##for i in li:
##    if i>10:
##        print(i,end=" ")



##
##li = [10, 20, 30, 40, 50, 60]
##count=0
##sum1=0
##for i in range(0,len(li),1):
##    count+=1
##    sum1+=li[i]
##   
##

##print("avg:--",sum1/count)

##
##li = [1,2,3,4,5,6,8,9,10]
##
##for i in range(1,len(li)+2):
##    if i not in li:
##        print(i)
##    



##li = [5, 12, 8, 20, 3, 15, 7]
##
##sam = li[0]
##
##for i in li:
##    if sam>i:
##        sam=i
##
##li.remove(sam)
##
##sam1 = li[0]
##
##for i in li:
##    if sam>i:
##        sam1=i
##
##print(sam1)

##li= [0, 1, 0, 3, 12]
##
##li2=[]
##count=0
##
##for i in li:
##    if i==0:
##        count+=1
##    else:
##        li2.append(i)
##
##
##for i in range(count):
##    li2.append(0)
##
##
##print(li2)
##    



##li = [1, 2, 3, 4, 5, 6]
##
##
##li1 = li[-1]
##
##li2 = li[-2]
##
##
##li.pop()
##
##li.pop()
##
##li.insert(0,li2)
##
##li.insert(1,li1)
##
##print(li)
##



##li = [1, 2, 3, 4, 5, 6]
##
##
##li1 = li[-1]
##
##li2 = li[-2]
##
##li3 = li[-3]
##
##li.pop()
##li.pop()
##li.pop()
##
##li.insert(0,li3)
##
##li.insert(1,li2)
##
##li.insert(2,li1)
##
##
##print(li)


##
##li = [2, 6, 8, 12, 14, 18, 20]
##count = 0
##for i in li:
##    if i%2==0 and i%3==0:
##        count+=1
##
##print(count)

##
##li = [10, 15, 20, 25, 30, 35, 40]
##
##for i in li:
##
##    if i%2==0 and i%5==0:
##        print(i)
##        break


##        
##count = 0 
##li = [10, 5, 12, 3, 4, 11, 2, 1]
##
##
##for i in li:
##    if i<10:
##        count+=1
##
##
##print(count)


##st = "pwwkew"
##
##li=""
##
##
##for i in st:
##    if i not in li:
##        li+=i
##
##print(li)
##    

##li = [2, 7, 11, 15, 3, 6]
##target = 9
##
##li1 = []
##
##for i in range(0,len(li),1):
##    for j in range(i+1,len(li)):
##        if li[i]+li[j]==target:
##            li1.append((li[i],li[j]))
##
##print(li1)
##            



li = [1, 2, 3, 2, 4, 5, 6, 1, 2]

li1 = []

for i in range(1,len(li),1):
    for j in range(i+1,len(li),2):
        if li[i]>li[j] and li[i] not in li1:
            li1.append(li[i])


            
print(li1)













