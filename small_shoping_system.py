##

##card = []
##
##while True:
####
##    print("\n1.View Avaliable Product \n2.Add Product to the cart \n3.Remove Product from the cart \n4.View the cart\n5.Calculate the total bill\n6.Exit the application")
##
##    choice = int(input("Enter your Choice:--"))
##
##    match(choice):
##
##        case 1:
##            
##            print("********************Product List********************\n")
##            li = [[1,"Iphone 12","4gb",1000],[2,"Iphone 13","4gb",12000],[3,"Iphone 14","4gb",130000],[4,"Iphone 15","5gb",140000],[5,"Iphone 15 Pro","16gb",145000],[6,"Iphone 15 Pro Max","12gb",150000]]
##            for i in li:
##                print(i)
##
##        case 2:
##            try:
##                user = int(input("Enter the Product Id:-"))
##                for i in range(0,len(li),1):
##                    
##                    if li[i][0]==user:
##                        card.append(li[i])
##                        print("Add Product Successfully")
##                    else:
##                          print("not present product")
##            except ValueError:
##                print("plz enter the a Int value")
##            
##          
##        case 3:
##            user2 = int(input("Enter the Product id to you have remove from list:-"))
##            for i in range(0,len(card),1):
##                    if card[i][0]==user2:
##                        card.remove(card[i])
##                        print("Remove product Successfully")
##            
##
##        case 4:
##            print("Your All Added Card:-",card)
##
##        case 5:
##            sum1=0
##
##            for i in range(0,len(card),1):
##                sum1+=card[i][3]
##
##            print("Your total Bil:--",sum1)
##
##        case 6:
##
##            break
##
##        case _:
##            print("Invalid Choice")

##    
##card = []
##
##while True:
##
##    print("\n1.View Avaliable Product \n2.Add Product to the cart \n3.Remove Product from the cart \n4.View the cart\n5.Calculate the total bill\n6.Exit the application")
##
##    choice = int(input("Enter your Choice:--"))
##
##    match(choice):
##
##        case 1:
##            
##            print("********************Product List********************\n")
##            li = [[1,"Iphone 12","4gb * 128 RAM",1000,1],
##                  [2,"Iphone 13","4gb * 256",12000,1],
##                  [3,"Iphone 14","4gb * 128 RAM",130000,1],
##                  [4,"Iphone 15","5gb",140000,1],
##                  [5,"Iphone 15 Pro","16gb",145000,1]
##                  ,[6,"Iphone 15 Pro Max","12gb",150000,1]]
##            for i in li:
##                print("                                    ",i)
##
##        case 2:
##            try:
##                user = int(input("Enter the Product Id:-"))
##                product_id = list(map(lambda x:x[0],li))
##                card_item= list(map(lambda x:x[0],card))
##
##                if user not in product_id:
##                    print("Not present Product id")
##                    
##                elif user in card_item:
##                    quantity = int(input("Enter the quantity:-"))
##                    for i in range(0,len(card),1):
##                        card[i][4]+=quantity
##                        
##                    
##                else:
##                    quantity1 = int(input("Enter the quantity:-"))
##                    for i in range(0,len(li),1):
##                        if li[i][0]==user:
##                            card.append(li[i])
##                            
##                            print("Add Product Successfully")
##            
##                
##            except ValueError:
##                print("plz enter the a Int value")
##            
##          
##        case 3:
##            user2 = int(input("Enter the Product id to you have remove from list:-"))
##            for i in range(0,len(card),1):
##                    if card[i][0]==user2:
##                        card.remove(card[i])
##                        print("Remove product Successfully")
##            
##
##        case 4:
##            print("Your All Added Card:-",card)
##
##        case 5:
##            sum1=0
##
##            for i in range(0,len(card),1):
##                sum1+=card[i][3]
##
##            print("Your total Bil:--",sum1)
##
##        case 6:
##
##            break
##
##        case _:
##            print("Invalid Choice")



cart = []
li =[
    [1, "Iphone 12", "4G * 128 RAM", 1000],
    [2, "Iphone 13", "4G * 256", 12000],
    [3, "Iphone 14", "4G * 128 RAM", 130000],
    [4, "Iphone 15", "5G * 256GB RAM", 140000],
    [5, "Iphone 15 Pro", "16G * 256GB RAM", 145000],
    [6, "Iphone 15 Pro Max", "12G * 1TB RAM", 150000],

    [7, "Iphone 11", "4G * 64GB RAM", 45000],
    [8, "Iphone 11 Pro", "4G * 256GB RAM", 55000],
    [9, "Iphone 12 Mini", "4G * 64GB RAM", 60000],
    [10, "Iphone 12 Pro", "4G * 256GB RAM", 75000],
    [11, "Iphone 12 Pro Max", "4G * 512GB RAM", 85000],
    [12, "Iphone 13 Mini", "5G * 128GB RAM", 70000],
    [13, "Iphone 13 Pro", "5G * 256GB RAM", 95000],
##    [14, "Iphone 13 Pro Max", "5G * 512GB RAM", 110000],
##    [15, "Iphone 14 Plus", "5G * 128GB RAM", 90000],
##    [16, "Iphone 14 Pro", "5G * 256GB RAM", 115000],
##    [17, "Iphone 14 Pro Max", "5G * 512GB RAM", 125000],
##    [18, "Iphone 15 Plus", "5G * 128GB RAM", 105000],
##    [19, "Iphone 15 Pro Max", "5G * 512GB RAM", 155000],
##    [20, "Iphone 16", "5G * 128GB RAM", 80000],
##    [21, "Iphone 16 Plus", "5G * 256GB RAM", 100000],
##    [22, "Iphone 16 Pro", "5G * 256GB RAM", 120000],
##    [23, "Iphone 16 Pro Max", "5G * 512GB RAM", 145000],
##    [24, "Iphone 16 Pro Max", "5G * 1TB RAM", 165000],
##    [25, "Iphone 17", "5G * 256GB RAM", 135000],
##    [26, "Iphone 17 Pro Max", "5G * 1TB RAM", 175000]
]




while True:

    print("\n1.View Avaliable Product \n2.Add Product to the cart \n3.Remove Product from the cart \n4.View the cart\n5.Calculate the total bill\n6.Exit the application")

    choice = int(input("Enter your Choice:--"))

    match(choice):

        case 1:
            
            print("********************Product List********************\n")

            for i in li:
                print("                                    ",i)

        case 2:
            try:
                user = int(input("Enter the Product Id:-"))
                product_id = list(map(lambda x:x[0],li))
                card_item= list(map(lambda x:x[0],cart))

                if user not in product_id:
                    print("Not present Product id")
                    
                elif user in card_item:
                    print("product already in cart")
                    quantity = int(input("Enter the quantity:-"))
                    for i in range(0,len(cart),1):
                        cart[i][4]+=quantity
                        
                    
                else:
                    li2 = []
                    for i in range(0,len(li),1):
                        if li[i][0]==user:
                            quantity = int(input("enter the quantity:-"))
                            li2.append(li[i][0])
                            li2.append(li[i][1])
                            li2.append(li[i][2])
                            li2.append(li[i][3])
                            li2.append(quantity)
                            
                    
                    cart.append(li2)
                    print("Add Product Successfully")
                    print(cart)
            
                
            except ValueError:
                print("plz enter the a Int value")
            
          
        case 3:
            user2 = int(input("Enter the Product Id to you have remove from cart:-"))
            cart_items = list(map(lambda x:x[0],cart))
            if user2 in cart_items:
                for i in range(0,len(cart),1):
                        if cart[i][0]==user2:
                            cart.remove(cart[i])
                            print("Remove product Successfully")
            else:
                print("\n \t \t Item is not present card")
            

        case 4:
            print("\nYour All Added Card:-")
            for i in cart:
                print(f"PID:-{i[0]} Name:-{i[1]} Ram:{i[2]} Price:-{i[3]} Quantity:-{i[4]}")

        case 5:
            sum1=0

            for i in range(0,len(cart),1):
                sum1+=(cart[i][3]*cart[i][4])

            print("Your total Bil:--",sum1)

        case 6:

            break

        case _:
            print("\nInvalid Choice")



##
##num = 8
##
##target = 0
##
##for i in range(1,num):
##    if num%i==0:
##        target+=i
##
##if target == num:
##    print("strong number")
##else:
##    print("not")





# #li = {
# #        1: ["Iphone 12", "4G * 128 RAM", 1000],
# #        2: ["Iphone 13", "4G * 256", 12000],
# #        3: ["Iphone 14", "4G * 128 RAM", 130000],
# #        4: ["Iphone 15", "5G * 256GB RAM", 140000],
# #        5: [ "Iphone 15 Pro", "16G * 256GB RAM", 145000],
# #        6: ["Iphone 15 Pro Max", "12G * 1TB RAM", 150000]
# #        }

##cart = {}
##keys1 = li.keys()
##values1 = li.values()
##
##def View_Product():
##
##    for i,j in li.items():
##        print(i,j)
##
##View_Product()
##
##def Add_Product():
##    user = int(input("enter the Product ID:"))
##
##    if user not in keys1:
##        print("Product not peresent")
##
##    elif user not in cart.keys():
##        q = int(input("enter the q:-"))
##        li2=li[user]
##        li2.append(q)
##        cart[user]=li2
##        print(cart)
##
##    else:
##        q = int(input("enter the q1:_"))
##        cart[user][3]+=q
##        print(cart)
##
##    
##
##Add_Product()
##
##
##def remove():
##    user = int(input("enter the a prodcut is:-"))
##
##    if user in cart.keys():
##        cart.pop(user)
##
####remove()
##
##
##def view():
##
##    for i,j in cart.items():
##        print(i,j)
##
##view()
##
##
##def total():
##
##    sum1 += (cart




























