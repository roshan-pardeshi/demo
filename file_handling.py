


##file = open("python.txt","x")

##file = open("python.txt","w")
##
##file.write("roshan\n pardeshi")
##
##file.close()

##
##file = open("python.txt","r")
##print(file.read())
##
##file.close()


##file = open("python.txt","a",)
##
##file.write("\njava\npython\n")
##
##file.close()
##
##file = open("python.txt","r")
##print(file.read())
##
##file.close()





##file = open("python.txt","w")
##
##
##file.write("\ndata science\npython development\nml engineer\nnlp developer")
##
##file.close()
##
##
##file = open("python.txt","r")
##
##data=file.readlines()
##count=0
##
##print(type(data))
##
##print(data)
##
##
##
##for i in range(0,len(data),1):
##    for j in range(0,len(data[i]),1):
##        count+=1
##    
##
##print(count)
##file.close()
##
##


##
##file = open("python.txt","r")
##
##print(file.readlines())
##
##file.close()

##file = open("python.txt","r")
##
##data = file.read()
##
##file1 = open("python1.txt","x")
##
##file2 = open("python1.txt","w")
##
##file2.write(data)
##
##file.close()
##file1.close()
##file2.close()


##file = open("python.txt","r")
##
##data=file.readlines()
##
####data = int(data)
##
####print(type(data[1]))
##sum1=0
##for i in data:
##    sum1+=int(i)
##
##
##print(sum1)
##file.close()


##file = open("python.txt","r")
##
####tu = ("a","i","e","o","u")
##
##for i in file.readlines():
##
##    if i.startswith("a") or i.startswith("e") or i.startswith("i") or i.startswith("o") or i.startswith("u"):
##        print(i)
##
##file.close()



##file = open("python.txt","r")
##
##data=file.readlines()
##
##for i in data:
##    if data[i]=="athu":
##        print("hello")
##        contineus
##
##file.close()


##li = [1,2,3,4,5,6,7]
####
####res = list(map(lambda x:x*x,li))
####
####print(res)
##
##
##res = list(filter(lambda x:x%2==0,li))
##
##print(res)


##li = ["apple","banana","kiwi","pear"]
##
##res = list(filter(lambda x:len(x)>4,li))
##
##print(res)


##cel = [0,20,3,100]
##
##res = list(map(lambda x:(x*(9/5)+32),cel))
##
##
##print(res)


##li = [12,15,20,22,29,30]
##
##
##res = list(filter(lambda x:x%5==0 and x%10!=0,li))
##
##print(res)


##
##li = ["python","java","c language","c++"]
##
##res = list(map(lambda x:len(x),li))
##
##print(res)




##tu = (10,20,30,40,50)
##
##res = tuple(map(lambda x:str(x),tu))
##
##print(res)

##
##tu = (3,9,12,18,17,21,25)
##
##
##res = tuple(filter(lambda x:x%3==0,tu))
##
##print(res)



##tu = (1,2,-1,-2,4,2,-5,-7)
##
##res = tuple(map(lambda x:x*(-1) if x<0 else x,tu))
##
##print(res)
##
##
####tu = (12,13,33,19,93,10)
####
####res = tuple(map(lambda x:x%10==3,tu))
####
####print(res)
##
##
##
##
##def prime(n):
##    num = n
##
##    factor = 0
##    for i in range(2,num-1,1):
##        if num%i==0:
##            factor+=1
##
##    if factor==0:
##        print(num)
##
##    
##
##
##
##se = {1,2,3,4,5,6,7,8,9,10}
##
##for i in range(1,len(se),1):
##    res = set(map(lambda x:prime(x),se))
##    break
##
####print(res)
##



##se = {1,2,3,4,5,6,7,8,9,10}
##
##res = set(map(lambda x:x**0.5,se))
##
##print(res)


##se = {100,200,300,400,500,600,700,800}
##
##
##res = set(filter(lambda x:x>300,se))
##
##print(res)

##
de = {"a":5,"b":12,"c":13,"d":15,"e":16,"f":10}
##
##
##res = dict(filter(lambda x:x[1]>15,de.items()))
##
##print(res)

##res = dict(map(lambda x:(x[0],x[1]**3),de.items()))
##
##print(res)

##de = {"apple":100,"banana":200,"cherry":300}
##
##res = dict(map(lambda x:(x[0].upper(),x[1]),de.items()))
##
##print(res)
##
##marks = {"ravi":70,"aman":75,"kiran":67,"pooja":90}
##
##res = dict(filter(lambda x:x[1]>70,marks.items()))
##
##print(res)


de = {"pen":10,"book":55,"pencil":5,"bag":500}

res = dict(map(lambda x:(x[0],x[1]-(x[1]*10)/100),de.items()))

print(res)







































































































































