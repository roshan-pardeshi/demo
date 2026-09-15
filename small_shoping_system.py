##
##
####card = []
####
####while True:
######
######    print("\n1.View Avaliable Product \n2.Add Product to the cart \n3.Remove Product from the cart \n4.View the cart\n5.Calculate the total bill\n6.Exit the application")
####
####    choice = int(input("Enter your Choice:--"))
####
####    match(choice):
####
####        case 1:
####            
####            print("********************Product List********************\n")
####            li = [[1,"Iphone 12","4gb",1000],[2,"Iphone 13","4gb",12000],[3,"Iphone 14","4gb",130000],[4,"Iphone 15","5gb",140000],[5,"Iphone 15 Pro","16gb",145000],[6,"Iphone 15 Pro Max","12gb",150000]]
####            for i in li:
####                print(i)
####
####        case 2:
####            try:
####                user = int(input("Enter the Product Id:-"))
####                for i in range(0,len(li),1):
####                    
####                    if li[i][0]==user:
####                        card.append(li[i])
####                        print("Add Product Successfully")
####                    else:
####                          print("not present product")
####            except ValueError:
####                print("plz enter the a Int value")
####            
####          
####        case 3:
####            user2 = int(input("Enter the Product id to you have remove from list:-"))
####            for i in range(0,len(card),1):
####                    if card[i][0]==user2:
####                        card.remove(card[i])
####                        print("Remove product Successfully")
####            
####
####        case 4:
####            print("Your All Added Card:-",card)
####
####        case 5:
####            sum1=0
####
####            for i in range(0,len(card),1):
####                sum1+=card[i][3]
####
####            print("Your total Bil:--",sum1)
####
####        case 6:
####
####            break
####
####        case _:
##            print("Invalid Choice")

    
##card = {}
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
##            li = [[1,"Iphone 12","4gb",1000],[2,"Iphone 13","4gb",12000],[3,"Iphone 14","4gb",130000],[4,"Iphone 15","5gb",140000],[5,"Iphone 15 Pro","16gb",145000],[6,"Iphone 15 Pro Max","12gb",150000]]
##            for i in li:
##                print(i)
##
##        case 2:
##            try:
##                user = int(input("Enter the Product Id:-"))
##                quantity = 90
##
##                for i in range(0,len(card),1):
##                    if card[i][0]==user:
##                        card.append(quantity)
##
##                    else:
##                        for i in range(0,len(li),1):
##                                if li[i][0]==user:
##                                    card.append(li[i])
##                                    print("Add Product Successfully")
##                                else:
##                                    print("not present")
##
##                
##            except ValueError:
##                print("plz enter the a Int value")
##            
##          
##        case 3:
##            user2 = int(input("Enter the Product id to you have remove from list:-"))
##            for i in range(0,len(card),1):
##                    if card[i][0]==user2 and card[i][0] in user2:
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
##
##
##
##
##
##
## 
####li = {1:["Iphone 12","4gb",1000],2:["Iphone 13","4gb",12000],3:["Iphone 14","4gb",130000],4:["Iphone 15","5gb",140000],5:["Iphone 15 Pro","16gb",145000],6:["Iphone 15 Pro Max","12gb",150000]}
##a = li.values()
##
##
##def View_Product():
##    print(li.items())
##
##View_Product()










































