
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
        user1 = input("Enter the a room facilities:-- \n 1.Single \n 2.Double \n 3.Deluxe:--")

        Rooms_Facilities = list(map(lambda x:x[1],rooms))
        
       
        if user1 in Rooms_Facilities:
            print("Currently this Rooms are Available For You")
            for i in range(0,len(rooms),1):
                    if rooms[i][3]=="Available" and rooms[i][1]==user1:
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
            if User in Rooms_id:
                Name = input("\nEnter your name :--")
                Address = input("\nEnter the address:--")
                days = int(input("\nHow many days you Stay Here:--"))
                sign_in_day = input("\nEnter Your Sign In date And Sign Out date:--")

                for i in range(0,len(rooms),1):
                    if rooms[i][3]=="Available" and rooms[i][0]==User:
                        li1.append(Name)
                        li1.append(Address)
                        li1.append(rooms[i][0])
                        li1.append(rooms[i][1])
                        li1.append(rooms[i][2])
                        li1.append(sign_in_day)
                        li1.append(days)
        

            Book_Room.append(li1)
            print("\n Room Book Successully")
            
    except ValueError:
        print("\nPlz enter chareter value")



def Sign_Out():
    sum1 = 0
    for i in range(0,len(Book_Room),1):
        sum1 +=(Book_Room[i][4]*Book_Room[i][6])

    print("\nYour  are Total Bil is a :--",sum1)

    if sum1==0:
        print("\nNo Any Room Book")
    else:
        print("\nThank You Sir Have a nice day...!")
    
def Booked_Room():

    for i in Book_Room:
        print(f"\n Name :--{i[0]} Address:-{i[1]} Room_Id:--{i[2]} Room_Type:--{i[3]} Room_Price:--{i[4]} Sign In/Sign Out:-{i[6]}")



while True:

    print("""\n    1. Check which type of you Find
             \n    2. View Room Series
             \n    3. Book your Room
             \n    4. Sign Out
             \n    5. View your Booked room
             \n    6. Exit 

             """)

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
            print("\nThank For you over website...!")
        case _:
            print("Invalid Choice")


    













        
