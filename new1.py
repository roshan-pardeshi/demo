


##
##
##
##li = ["roshan","tushar","roshan","roshan","swarup"]
##
##
##for i in range(0,len(li),1):
##    if li[i]=="roshan":
##        li.append("xyz")
##
##print(li)
        



cart ={}
d1 = {1:["Iphone 13",2000],
      2:["Iphone 14",3000],
      3:["Iphone 15",5000],
      4:["Iphone 16",6000]
      }
d2 = d1.keys()
##
##def view_product():
##
##    for i in d1.items():
##        print("\n ",i)
##
##view_product()
##
##
##def Add_cart():
##
##    user = int(input("Enter the number:-"))
##
##    if user not in d2:
##        print("Product not present")
##
##    elif user in cart:
##        print("****product present in cart*****")
##        quality = int(input("Enter the a Qunatity"))
##        
##        for i in cart.values():
##            cart[i][1]+=quality
##
##    else:
##        user = int(input("Enter the number:-"))
##        cart[user]=d1[user]
##
##       
##        print(cart)
##Add_cart()



























li = ["a","b","a","b","c","d","a"]


##for i in range(0,len(li),1):
##li[i].replace("a","rr")

res=list(map(lambda x:x.replace("a","rr"),li))

print(res)
        






































