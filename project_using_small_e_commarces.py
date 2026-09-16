

cart = []

li = [[1,"vivo",10000],
      [2,"oppo",120000],
      [3,"Iphone",150000],
      [4,"Redmi",13000],
      [5,"Realmi",140000],
      [6,"Sumsung",144000],
      [7,"Nokiya",5000000]
      ]


def View_Product():
    
    print(" *==============================================================================================================*\n")
    print("===================================================Product List===================================================\n")
    print(" *==============================================================================================================*\n")
     
    for i in li:
        print("     ",i)


def Add_Product():
    try:
        user = int(input("Enter the Product Id:-"))

        Product_li = list(map(lambda x:x[0],li))
        Cart_li = list(map(lambda x:x[0],cart))
      
                              
        if user not in Product_li:
            print("Product Not Present in Mart")

        elif user in Cart_li:
            print("====================================================Product all ready  Added in cart====================================================")
            quantity = int(input("Enter the a Qantity:-"))
            for i in range(0,len(cart),1):
                cart[i][3]+=quantity

        else:
            li2 = []
            for i in range(0,len(li),1):
                if li[i][0]==user:
                    quantity = int(input("Enter the Quantity:-"))
                    li2.append(li[i][0])
                    li2.append(li[i][1])
                    li2.append(li[i][2])
                    li2.append(quantity)


            cart.append(li2)
            print("Product Add Successfully")
            
    except ValueError,IndexError:
        print("\n Error")

            

def View_Cart():
    print(" *====================================================================================================*\n")
    print("==============================================Added Cart==============================================\n")
    print(" *=====================================================================================================*\n")
        
    for i in cart:
        print("\n",f"PID :-- {i[0]} Product Name :-- {i[1]} Product Price :-- {i[2]} Product Qunatity :-- {i[3]}")
    

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

    print("\n1.View Product list\n2.Add Product\n3.View Added Product\n4.Remove Product From Cart\n5.Product Bill\n6.Exit Application")

    Choice = int(input("Enter Your Choice :--"))

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

        case _:
            print("\n====================================================Invalid Choice====================================================")











