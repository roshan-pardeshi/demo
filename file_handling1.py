##
##
##def write():
##    file = open("python2.txt","w")
##
##    file.write("101 roshan 35\n102 pratik 37\n103 tushar 36\n104 abhay 37")
##
##    file.close()
##
##write()

##
##file = open("python1.txt","r")
##
##print(file.read())
##
##file.close()


##import os
##
##
##os.rename("python2.txt","python3.txt")

##
##file = open("python3.txt","r")
##
##print(file.read())
##
##file.close()


##os.remove("python3.txt")

##file = open("python1.txt","r+")
##
##file.readline()
##
##print(file.readline())
##
####print(file.tell())
##
##file.seek(34)
##
##file.write("vasudha ")
##
##file.close()







##file = open("python1.txt","r")
##
##data = file.read()
##
##data = data.replace("vasudha ","Vasudha ")
##
##file.close()

##
##

def read_student(n):

    file = open("python1.txt","r")

   data = file.readlines()


   for i in data:
       print(i)

       
    file.close()

read_student(n)
def add_student(n):
    file = open("python1.txt","a")

    

    for i in range(n):
        roll_no = input("enter the new roll_number")
        name_of_student = input("Enter The New Student Name")
        marks_of_student = input("Enter The Marks of The Student")
        
    file.write(f"{roll_no} {name_of_student} {marks_of_student} \n")

    file.close()


    file = open("python1.txt","r")

    print(file.read())

    file.close()

##n = int(input("Enter How Many Student You Add"))
##add_student(n)

def modify_student_record(rename_student_name,roll_number,rename_name):
    file = open("python1.txt","r+")
    data = file.readlines()
    f1=[]
    for i in range(0,len(data),1):
        data1 = data[i].split()

        temp=[]

        for j in range(0,len(data1),1):
            if data1[j]==rename_student_name and data1[j-1]==roll_number:
                temp.append(rename_name)
            else:
                temp.append(data1[j])

        f1.append(" ".join(temp)+"\n")
        


    file1 = open("python1.txt","w")
    file1.writelines(f1)

    file1.close()
    file.close()
    file3 = open("python1.txt","r")
    print(file3.read())
    file3.close()


##modify_student_record(input("enter the name of student to you remove from your record:--"),input("enter the rollnumber:--"),rename_name = input("enter the rename name Here:--"))


def remove_student():
    file = open("python1.txt","r+")

    data = file.readlines()

    ##print(data)

    f1 = []

    for i in range(0,len(data),1):
        data1 = data[i].split()

        temp=[]
        for j in range(0,len(data1),1):
            if data1[j]=="krishna" and data1[j-1]=="106" and data1[j+1]=='78':
                temp.pop()
            else:
                temp.append(data1[j])

        f1.append(" ".join(temp)+'\n') 

    file1 = open("python1.txt","w")

    file.writelines(f1)

    file.close()


    file.close()




##read_student()












































