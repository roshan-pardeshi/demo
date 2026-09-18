

##cart = []
##
##li = [[1,"vivo",10000],
##      [2,"oppo",120000],
##      [3,"Iphone",150000],
##      [4,"Redmi",13000],
##      [5,"Realmi",140000],
##      [6,"Sumsung",144000],
##      [7,"Nokiya",5000000]
##      ]
##
##
##def View_Product():
##    
##    print(" *==============================================================================================================*\n")
##    print("===================================================Product List===================================================\n")
##    print(" *==============================================================================================================*\n")
##     
##    for i in li:
##        print("     ",i)
##
##
##def Add_Product():
##    try:
##        user = int(input("Enter the Product Id:-"))
##
##        Product_li = list(map(lambda x:x[0],li))
##        Cart_li = list(map(lambda x:x[0],cart))
##      
##                              
##        if user not in Product_li:
##            print("Product Not Present in Mart")
##
##        elif user in Cart_li:
##            print("====================================================Product all ready  Added in cart====================================================")
##            quantity = int(input("Enter the a Qantity:-"))
##            for i in range(0,len(cart),1):
##                cart[i][3]+=quantity
##
##        else:
##            li2 = []
##            for i in range(0,len(li),1):
##                if li[i][0]==user:
##                    quantity = int(input("Enter the Quantity:-"))
##                    li2.append(li[i][0])
##                    li2.append(li[i][1])
##                    li2.append(li[i][2])
##                    li2.append(quantity)
##
##
##            cart.append(li2)
##            print("Product Add Successfully")
##            
##    except ValueError,IndexError:
##        print("\n Error")
##
##            
##
##def View_Cart():
##    print(" *====================================================================================================*\n")
##    print("==============================================Added Cart================================================\n")
##    print(" *=====================================================================================================*\n")
##        
##    for i in cart:
##        print("\n",f"** PID :-- {i[0]} Product Name :-- {i[1]} Product Price :-- {i[2]} Product Qunatity :-- {i[3]} **")
##    
##
##def Remove_Product():
##    try:
##        user = int(input("Enter the Product Id to you have try to remove:-"))
##
##        Cart_id = list(map(lambda x:x[0],cart))
##
##        if user in Cart_id:
##            for i in range(0,len(cart),1):
##                cart.remove(cart[i])
##
##            print("\n====================================================Product Remove Successfully====================================================")
##
##        else:
##            print("Product Not Present")
##            
##    except ValueError:
##        print("\n====================================================Invalid Input====================================================")
##
##
##def Total_Bil():
##    sum1 = 0
##
##    for i in range(0,len(cart),1):
##        sum1 +=(cart[i][2]*cart[i][3])
##
##    print("Total Bil:--",sum1)
##        
##
##
##    
##            
##
##while True:
##    try:
##
##        print("\n1.  View Product list\n\n2.  Add Product\n3.  View Added Product\n4.  Remove Product From Cart\n5.  Product Bill\n6.  Exit Application")
##
##        Choice = int(input("\nEnter Your Choice :--"))
##
##        if Choice>6 or Choice>=0:
##            match(Choice):
##                case 1:
##                    View_Product()
##
##                case 2:
##                    Add_Product()
##
##                case 3:
##                    View_Cart()
##
##                case 4:
##                    Remove_Product()
##
##                case 5:
##                    Total_Bil()
##
##                case 6:
##                    print("\n*====================================================Thank You Have a nice day!====================================================")
##                    break
##
##                case _:
##                    print("\n====================================================Invalid Choice====================================================")
##        else:
##            print("\nPlease enter valid choice")
##
##    except ValueError:
##        print("Please Enter Integer value Only")






cart = []

mobile = [
    [1, "iPhone 13", 55000],
    [2, "Samsung Galaxy S23", 62000],
    [3, "OnePlus 12", 58000],
    [4, "Google Pixel 8", 70000],
    [5, "Vivo V30", 35000],
    [6, "Redmi Note 13", 22000],
    [7, "Realme 12 Pro", 28000],
    [8, "Nothing Phone 2", 40000]
]

laptop = [
    [101, "HP Pavilion", 65000],
    [102, "Dell Inspiron", 58000],
    [103, "Lenovo IdeaPad", 52000],
    [104, "MacBook Air M2", 95000],
    [105, "ASUS VivoBook", 62000],
    [106, "Acer Aspire 5", 48000],
    [107, "HP Victus", 78000],
    [108, "Lenovo Legion 5", 115000]
]

bike = [[11,"Pulsar 125",12000],
        [22,"Royal Enfield Classic 350",225000],
        [33,"Yamaha MT-15",250000],
        [44,"Honda CB350",124000],
        [55,"KTM Duke",145000],
        [66,"Pulsar 220",200000]
        ]

shoes = [
    [201, "Nike Air Max", 8500],
    [202, "Adidas Ultraboost", 12000],
    [203, "Puma Running", 6500],
    [204, "Reebok Classic", 5500],
    [205, "Skechers Go Run", 7200],
    [206, "Campus Sports", 2500],
    [207, "Nike Revolution", 4800],
    [208, "Adidas Forum", 9000]
]

electronics = [
    [301, "Sony Bravia TV", 75000],
    [302, "Samsung Smart TV", 62000],
    [303, "LG OLED TV", 95000],
    [304, "JBL Speaker", 12000],
    [305, "Boat Headphones", 2500],
    [306, "Apple AirPods", 18000],
    [307, "Sony Headphones", 22000],
    [308, "Canon Camera", 55000]
]


def View_Product():
    
    print(" *==============================================================================================================*\n")
    print("===================================================Product List===================================================\n")
    print(" *==============================================================================================================*\n")
    print("1. ======== Mobile \n2. ====== Laptop \n3. ==== Bike\n4. == Shoes\n5. =electronics")
    choice = int(input("\nWhich Product You Seen:--"))
    match(choice):
        case 1:
            for i in mobile:
                print("\n     ",i)
        case 2:
            for i in laptop:
                print("\n     ",i)
        case 3:
            for i in bike:
                print("\n     ",i)
        case 4:
            for i in shoes:
                print("\n     ",i)
        case 5:
            for i in shoes:
                print("\n     ",i)
        case 6:
            for i in electronics:
                print("\n     ",i)

        case _:
            print("Invalid Choice")
                


def Add_Product():
    try:
        print("  *================================================================================================================================*\n")
        print("=========================================================Product Categories==========================================================\n")
        print("  *================================================================================================================================*\n")
        
        print("""
                1. ======== Mobile ID starting from 1 to 8
                2. ====== Laptop ID starting from 101 to 108
                3. ==== Bike ID starting from 11 to 66
                4. == Shoes ID starting from 201 to 208
                5. = Electronics ID starting from 301 to 308
                    """)

        choice = int(input("\nEnter the choice:-"))

        match(choice):
            case 1:
                
                for i in mobile:
                    print("\n   ",i)

                user = int(input("Enter the product Id"))
                mobile_id = list(map(lambda x:x[0],mobile))
                mobile_cart = list(map(lambda x:x[0],cart))

                

                if user not in mobile_id:
                    print("Product id not present")

                elif user in mobile_cart:
                    quantity = int(input("Enter the Quantity:-"))

                    for i in range(0,len(cart),1):
                        cart[i][3]+=quantity

                else:
                    quantity = int(input("enter the Quantity:--"))
                    li2=[]
                    
                    for i in range(0,len(mobile),1):
                        if mobile[i][0]==user:
                            li2.append(mobile[i][0])
                            li2.append(mobile[i][1])
                            li2.append(mobile[i][2])
                            li2.append(quantity)

                    cart.append(li2)
                    print("\nProduct add successfully")
                
            case 2:
                user = int(input("enter the product Id"))
                laptop_id = list(map(lambda x:x[0],laptop))
                laptop_cart = list(map(lambda x:x[0],cart))


                if user not in laptop_id:
                    print("Product id not present")

                elif user in laptop_cart:
                    quantity = int(input("Enter the Quantity:-"))

                    for i in range(0,len(cart),1):
                        cart[i][3]+=quantity

                else:
                    quantity = int(input("Enter the Quantity"))
                    li2=[]
                    for i in range(0,len(laptop),1):
                        if laptop[i][0]==user:
                            li2.append(laptop[i][0])
                            li2.append(laptop[i][1])
                            li2.append(laptop[i][2])
                            li2.append(quantity)

                    cart.append(li2)
                    print("\nProduct add successfully")

            case 3:

                user = int(input("Enter the a product ID:--"))
                bike_id = list(map(lambda x:x[0],bike))
                cart_id = list(map(lambda x:x[0],cart))

                if user not in bike_id:
                    print("Product not present in list")

                elif user in cart_id:
                    quantity = int(input("Enter the a Quantity:--"))
                    for i in range(0,len(cart),1):
                        cart[i][3]+=quantity

                else:
                    quantity = int(input("\nEnter the Quantity:--"))
                    li=[]
                    for i in range(0,len(bike),1):
                        if bike[i][0]==user:
                            li.append(bike[i][0])
                            li.append(bike[i][1])
                            li.append(bike[i][2])
                            li.append(quantity)

                    cart.append(li)
                    print("\nProduct add successfully")
                    
            case 4:
                user = int(input("Enter the a product ID:--"))
                shoes_id = list(map(lambda x:x[0],shoes))
                cart_id = list(map(lambda x:x[0],cart))

                if user not in shoes_id:
                    print("Product not present in list")

                elif user in cart_id:
                    quantity = int(input("Enter the a Quantity:--"))
                    for i in range(0,len(cart),1):
                        cart[i][3]+=quantity

                else:
                    quantity = int(input("\nEnter the Quantity:--"))
                    li=[]
                    for i in range(0,len(shoes),1):
                        if shoes[i][0]==user:
                            li.append(shoes[i][0])
                            li.append(shoes[i][1])
                            li.append(shoes[i][2])
                            li.append(quantity)

                    cart.append(li)
                    print("\nProduct add successfully")
            case 5:
                user = int(input("Enter the a product ID:--"))
                electronics_id = list(map(lambda x:x[0],electronics))
                cart_id = list(map(lambda x:x[0],cart))

                if user not in electronics_id:
                    print("Product not present in list")

                elif user in cart_id:
                    quantity = int(input("Enter the a Quantity:--"))
                    for i in range(0,len(cart),1):
                        cart[i][3]+=quantity

                else:
                    quantity = int(input("\nEnter the Quantity:--"))
                    li=[]
                    for i in range(0,len(electronics),1):
                        if electronics[i][0]==user:
                            li.append(electronics[i][0])
                            li.append(electronics[i][1])
                            li.append(electronics[i][2])
                            li.append(quantity)

                    cart.append(li)
                    print("\nProduct add successfully")
                
            case _:
                print("\n Invalid choice")
                
         
    except ValueError,IndexError:
        print("\n Error")

            

def View_Cart():
    print(" *====================================================================================================*\n")
    print("==============================================Added Cart================================================\n")
    print(" *=====================================================================================================*\n")
        
    for i in cart:
        print("\n",f"** PID :-- {i[0]} Product Name :-- {i[1]} Product Price :-- {i[2]} Product Quantity :-- {i[3]} **")
    

def Remove_Product():
    try:
        user = int(input("Enter the Product Id to you have try to remove:-"))

        Cart_id = list(map(lambda x:x[0],cart))

        if user in Cart_id:
            for i in range(0,len(cart),1):
                cart.remove(cart[i])

            print("\n====================================================Product Remove Successfully====================================================")

        else:
            print("Product Not Present")
            
    except ValueError:
        print("\n====================================================Invalid Input====================================================")


def Total_Bil():
    sum1 = 0

    for i in range(0,len(cart),1):
        sum1 +=(cart[i][2]*cart[i][3])

    print("Total Bil:--",sum1)
        


    
            

while True:
    try:

        print("\n1.  View Product list\n\n2.  Add Product\n\n3.  View Added Product\n\n4.  Remove Product From Cart\n\n5.  Product Bill\n\n6.  Exit Application")

        Choice = int(input("\nEnter Your Choice :--"))

        if Choice>6 or Choice>=0:
            match(Choice):
                case 1:
                    View_Product()

                case 2:
                    Add_Product()

                case 3:
                    View_Cart()

                case 4:
                    Remove_Product()

                case 5:
                    Total_Bil()

                case 6:
                    print("\n*====================================================Thank You Have a nice day!====================================================")
                    break

                case _:
                    print("\n====================================================Invalid Choice====================================================")
        else:
            print("\nPlease enter valid choice")

    except ValueError:
        print("Please Enter Integer value Only")















































