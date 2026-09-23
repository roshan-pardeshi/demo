import mysql.connector
rooms = [
    [101, "Single", 1000, "Available"],
    [102, "Single", 1000, "Booked"],
    [103, "Double", 1500, "Available"],
    [104, "Double", 1500, "Available"],
    [105, "Deluxe", 2000, "Booked"],
    [106, "Deluxe", 2000, "Available"],
    [107, "Deluxe", 2000, "Available"],
    [108, "Suite", 3500, "Booked"],
    [109, "Suite", 3500, "Available"],
    [110, "Suite", 3500, "Available"],
    [201, "Single", 1000, "Available"],
    [202, "Double", 1500, "Booked"],
    [203, "Deluxe", 2000, "Available"],
    [204, "Deluxe", 2000, "Available"],
    [205, "Suite", 3500, "Booked"]
]


def Check_Room_Available_in_Hotel():
    try:
        user2 = int(input("\n Over Rooms Starting from 1000 to 3500 \nEnter Your Buget:=="))
        user1 = input("Enter the a room facilities:-- \n 1.Single \n 2.Double \n 3.Deluxe:--")

        Rooms_Facilities = list(map(lambda x:x[1],rooms))
        
        if user1 in Rooms_Facilities:
            print("\nCurrently this Rooms are Available For You")
            for i in range(0,len(rooms),1):
                    if rooms[i][3]=="Available" and rooms[i][1]==user1 and rooms[i][2]<=user2:
                         print("\n    ",rooms[i])
        else:
            print("\nThis type of rooms are currently not available")

    except ValueError:
        print("\n Plz Enter the chareter Value")


Book_Room = []


Rooms_id = list(map(lambda x:x[0],rooms))



def View_Rooms_Details():

    for i in rooms:
        print("\n      ",i)




def Booking_Room():

    try:
    
        User = int(input("\nEnter the a Room Number:--"))

        Already_Book_Rooms_Id = list(map(lambda x:x[2],Book_Room))

        if User not in Rooms_id:
            print("Plz Enter valid room Number")

        elif User in Already_Book_Rooms_Id:
            print("\nSorry Sir this room already booked by other person")

        else:
            li1 = []
            try:
                if User in Rooms_id:
                    for i in range(0,len(rooms),1):
                        if rooms[i][0]==User and rooms[i][3]=="Available":
                            Name = input("\nEnter your name :--")
                            Address = input("\nEnter the address:--")
                            days = int(input("\nHow many days you Stay Here:--"))
                            sign_in_day = input("\nEnter Your Sign In date And Sign Out date:--")
                            li1.append(Name)
                            li1.append(Address)
                            li1.append(rooms[i][0])
                            li1.append(rooms[i][1])
                            li1.append(rooms[i][2])
                            li1.append(sign_in_day)
                            li1.append(days)
                            rooms[i][3]="Booked"
                    
                Book_Room.append(li1)
                print("\n Room Book Successully")
                file = open("python.txt","w")
                file.writelines(str(Book_Room))
                
##                sql_database()
                
                
            except ValueError:
                print("\nValue error occurs")
                
    except ValueError:
        print("\nPlz enter chareter value")






Food_veg2=[]
def Food_order():

    veg_food = [
        [1, "Veg Thali", 180],
        [2, "Paneer Butter Masala", 220],
        [3, "Paneer Tikka", 240],
        [4, "Mix Veg", 180],
        [5, "Veg Kolhapuri", 190],
        [6, "Palak Paneer", 210],
        [7, "Dal Tadka", 140],
        [8, "Jeera Rice", 120],
        [9, "Veg Biryani", 180],
        [10, "Butter Naan", 65]
        ]


    Non_veg_food = [
        [11, "Chicken Biryani", 220],
        [22, "Chicken Tikka", 250],
        [33, "Butter Chicken", 280],
        [44, "Chicken Handi", 260],
        [55, "Chicken Kolhapuri", 270],
        [66, "Mutton Biryani", 320],
        [77, "Mutton Curry", 350],
        [88, "Egg Curry", 160],
        [99, "Chicken Fried Rice", 200],
        [111, "Chicken Noodles", 210]
    ]
    

    while True:
        print("\n1. Veg Food\n2. Non Veg Food\n3. View Your Order\n4. View Total Bil\n5. Exit From Food Menu")
        choice1 = int(input("\nEnter your choice for Order:--"))
        
        try:
            match(choice1):

                case 1:
                    print("\n1. View Menu\n2. Order Food\n3. View Total Order")

                    choice2 = int(input("\nEnter Your Choice:---(Veg Food)---"))

                    match(choice2):
                     

                            case 1:
                                print("\n====================Veg Menu====================")
                                for i in veg_food:
                                    print("\n           ",i)
                            case 2:
                                user = int(input("Enter the food id:-"))
                                food_id = list(map(lambda x:x[0],veg_food))
                                food_book_id = list(map(lambda x:x[0],Food_veg2))

                                if user not in food_id:
                                    print("the id don't present in the a Menu")

                                elif user in food_book_id:
                                    print("\n Add more Quantity:")
                                    quantity = int(input("\nEnter the Quantity Food Dish:-"))
                                    for i in range(0,len(Food_veg2),1):
                                        Food_veg2[i][3]+=quantity

                                else:
                                    Food_veg = []
                                    for i in range(0,len(veg_food),1):
                                        if user == veg_food[i][0]:
                                            quantity = int(input("\nEnter the Quantity:--"))
                                            Food_veg.append(veg_food[i][0])
                                            Food_veg.append(veg_food[i][1])
                                            Food_veg.append(veg_food[i][2])
                                            Food_veg.append(quantity)


                                    Food_veg2.append(Food_veg)
                                    print("\n Order Book Succefully")
##                            case 3:
##                                for i in range(0,len(Food_veg2),1):
##                                    print(Food_veg[i])
                                   
                case 2:            
                    try:
                        
                            print("\n1. View Menu\n2. Order Food Non Veg Food")

                            choice3 = int(input("\nEnter Your Choice:---(Non Veg)---"))

                            match(choice3):
                                 
                                    case 1:
                                        print("\n====================Non Veg Menu====================")
                                        for i in Non_veg_food:
                                            print("\n           ",i)
                                            
                                    case 2:
                                        user = int(input("Enter the food id:-"))
                                        food_id = list(map(lambda x:x[0],Non_veg_food))
                                        food_book_id = list(map(lambda x:x[0],Food_veg2))

                                        if user not in food_id:
                                            print("the id don't present in the a Menu")

                                        elif user in food_book_id:
                                            print("\n Add more Quantity:")
                                            quantity = int(input("\nEnter the Quantity Food Dish:-"))
                                            for i in range(0,len(Food_veg2),1):
                                                Food_veg2[i][3]+=quantity

                                        else:
                                            Food_veg1 = []
                                            for i in range(0,len(Non_veg_food),1):
                                                if user == Non_veg_food[i][0]:
                                                    quantity = int(input("\nEnter the Quantity:--"))
                                                    Food_veg1.append(Non_veg_food[i][0])
                                                    Food_veg1.append(Non_veg_food[i][1])
                                                    Food_veg1.append(Non_veg_food[i][2])
                                                    Food_veg1.append(quantity)


                                            Food_veg2.append(Food_veg1)
                                            print("\n Order Book Succefully")
                    except Exception as e:
                        print("Order Error",e)
              
                case 3:
                    for i in Food_veg2:
                        print(i)


                case 4:
                    Sum1 = 0
                    for i in range(0,len(Food_veg2),1):
                        Sum1+=(Food_veg2[i][2]*Food_veg2[i][3])

                    print("Your Total bil of Food:--",Sum1)

                case 5:
                    print("Thank you For Order......!!")
                    break
                
        except Exception as e:
            print("Order Error",e)

def Sign_Out():
    sum1 = 0
    book_id = list(map(lambda x:x[2],Book_Room))
    for i in range(0,len(Book_Room),1):
        sum1 +=(Book_Room[i][4]*Book_Room[i][6])

    print("\nYour  are Total Bil is a :--",sum1)

    if sum1==0:
        print("\nNo Any Room Book")
    else:
        print("\nThank You Sir Have a nice day...!")

        for i in rooms:
            if book_id in i[0]:
                i[3]="Available"
            
    
def Booked_Room():

    for i in Book_Room:
        print(f"\n Name :--{i[0]} Address:-{i[1]} Room_Id:--{i[2]} Room_Type:--{i[3]} Room_Price:--{i[4]} Sign In/Sign Out:-{i[6]}")

while True:

    print("""\n    1. Check which type of you Find
             \n    2. View Room Series
             \n    3. Book your Room
             \n    4. Sign Out
             \n    5. View your Booked room
             \n    6. Order Food
             \n    7. Exit 

             """)

    try:
        Choice = int(input("\nEnter your Choice:--"))

        match(Choice):

            case 1:
                Check_Room_Available_in_Hotel()
                
            case 2:
                View_Rooms_Details()
                
            case 3:
                Booking_Room()

            case 4:
                Sign_Out()
                
            case 5:
                Booked_Room()

            case 6:
                Food_order()

            case 7:
                print("\nThank For you over website...!")
                break

                
            case _:
                print("\nInvalid Choice")
                
    except Exception as e:
        print("\nPlz Enter the currect choice",e)
            



    

##https://chocolate-candy-c79.notion.site/Youtube-Internship-roadmap-3dfd8c33330f806ca8f9df8090d3686a





##volume
##
##velocity
##
##variety
##
##veracity
##
##value


        
