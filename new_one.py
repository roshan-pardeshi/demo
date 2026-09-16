
li = [[1,"Iphone 13",100000],[2,"Iphone 13 Pro",110000],[3,"Iphone 14",120000],[4,"Iphone 14 Pro",130000]]


def View_Product():
    print("\n********************Product List********************\n")
    for i in li:
        print(i)

cart = []

def Add_Cart():

    try:
        user = int(input("Enter the Product Id:--"))

        # For  stored the a Product ID
        li1=[]
        for i in li:
            li1.append(i[0])

        # For stored the Cart ID
        li2=[]
        sum1=0
        for i in cart:
            li2.append(i)
            print(i)

        # check the id is present in cart or not 
        if user in li1:

            #check the id is preset already perent in a cart then increase it 
            if user in li2:
               quantity = int(input("Enter the Quantity:-"))
               cart.append(quantity)

            #if id not present add it product
               
            else:
                for i in range(0,len(li),1):
                    if li[i][0]==user:
                        cart.append(li[i])
##                        cart.append(quantity)

                for i in range(0,len(cart),1):
                    sum1+=1

                cart.append(sum1)
        else:
            print("\n     /// Product Id is Not Present \\\     ")
                        
    except Exception as e:
        print("Error:",e)


def Remove_Cart():
    
    user = int(input("Enter the Product id you try to remove:-"))
    for i in range(0,len(li),1):
        if li[i][0]==user:
            cart.remove(li[i])
            

def Total_bill():
    sum1 = []

    for i in range(0,len(cart),1):
        sum1.append(cart[i])

    print(sum1)

##    for i in range(0,len(cart),1):
##        if cart[i
def View_Cart():
    print(cart)


while True:

    print("\n1.View Available Product\n2.Add Product to the Cart\n3.Remove Product Frome the Cart\n4.View the Cart\n5.Calulate the total bill\n6.Exit the application")

    choice = int(input("Enter your choice"))

    match(choice):

        case 1:
            View_Product()

        case 2:
            Add_Cart()

        case 3:
            Remove_Cart()

        case 4:
            View_Cart()

        case 5:
            Total_bill()

        case 6:
            break

        case _:
            print("Invalid choice")













            
