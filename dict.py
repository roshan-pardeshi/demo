


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



li  =[[2,3,1],[3,2,5],[1,2]]

sum1 = []


for i in li:
    sum1.append(sum(i))
        
a = sorted(sum1)

print(a[-1])
