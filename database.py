##
##
##import mysql.connector as ms
##
##
##data = ms.connect(host="localhost",user="root",password="mysql@123",database="python_batch")
##
##
##cursor1 = data.cursor()
##
##li = [1,"roshan",9423664345,"he is good boy","so nice"]
##
##values = []
##
##for i in li:
##    values.append(i)
##
##
##insert_data = "insert into r_p(id,name,mob_no,feed_back,chart_data) values(%s,%s,%s,%s,%s)"
##
##cursor1.executemany(insert_data,(values,))
##
##data.commit()
##
##
##delete_data = "delete from r_p where id=1"
##
##
##
##cursor1.execute(delete_data)
##cursor1.close()




##di = {
##    "roshan pardeshi":"hi is a good boy",
##    
##    "vasudha bhawar":"she is a friend of roshan",
##    
##    "tushar patil":"hi is mc",
##    
##    "krishna su":"his computer science student",
##    
##    "mohit patil":"hi is a data realited work hi handle",
##    
##    "what is the hotel name": "Welcome to Royal Palace Hotel.",
##    
##    "where is the hotel located": "Royal Palace Hotel is located in Pune, Maharashtra.",
##    
##    "what rooms are available": "We have Single, Double, Deluxe and Suite rooms.",
##    
##    "what is the single room price": "The Single Room costs Rs. 1500 per night.",
##    }
##
##
##while True:
##    li = []
##
##    for i in di.keys():
##        li.append(i)
##
##    user = input("enter the choice").lower()
##
##    for i in li:
##        if user in i:
##            print(i," : ",di[i])
##            break
####
##


##li = [1,2,1,2,3,4,5,3,4,1,3,5]
##
##li1=[]
##for i in li:
##    count = li.count(i)
##
##    if i not in li1:
##        print(i," : ",count)
##        li1.append(i)
##        



##
##li = [1,2,3,4,5,2,1]
##
##
##li1= []
##
##
##for i in li:
##    count = li.count(i)
##
##    if count>1 and i not in li1:
##        li1.append(i)
##
##
##
##print(li[-1])

##st = "aabbcccd"
##
##for i in st:
##    count = st.count(i)
##
##    if count==1:
##        print(i)


##st = "aaabbccaa"
##
##size = ""
##
##for i in st:
##    if i not in size:
##        size+=i
##print(size)





di = {
    "roshan pardeshi":"hi is a good boy",
    
    "vasudha bhawar":"she is a friend of roshan",
    
    "tushar patil":"hi is mc",
    
    "krishna su":"his computer science student",
    
    "mohit patil":"hi is a data realited work hi handle",
    
    "what is the hotel name": "Welcome to Royal Palace Hotel.",
    
    "where is the hotel located": "Royal Palace Hotel is located in Pune, Maharashtra.",
    
    "what rooms are available": "We have Single, Double, Deluxe and Suite rooms.",
    
    "what is the single room price": "The Single Room costs Rs. 1500 per night.",
    }


##while True:
##li = []
##
##for i in di.keys():
##    li.append(i)
##
####user = input("enter the choice").lower()
##
##user ="roshan"
##
##li1 = []
##for i in user:
##    li1.append(i)
##
##
##print(li1)
##    
##
##
##for i in li:
####    if i in li1:
##    if user in i:
##        print(di[i])







        











