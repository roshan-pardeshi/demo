##
##
##li  = [1,2,3,4,5,1,2,3,4,5,6,1]
##
##
##fr = {}
##
##for i in li:
##    if i in fr.keys():
##        fr[i]+=1
##
##    else:
##        fr[i]=1
##
##print(fr)

##st = 'listen'
##
##st1 = "slien"
##isan = False
##if len(st) == len(st1):
##    for i in range(0,len(st),1):
##        if st[i] in st1:
##            isan = True
##        else:
##            isan = False
##
##
##if isan :
##    print(isan)
##else:
##    print("not")
li = [100,2000,10034030,139290,139290,1324]

li1 = []


for i in li:
    if i not in li1:
        li1.append(i)

        
a = sorted(li1)

print(a[-1]+a[-2])
##
##
##li = ["a","b","a","b","a","a","r"]
##
##
##res = list(map(lambda x:x.replace("a","roshan"),li))
##
##print(res)
##
##

































