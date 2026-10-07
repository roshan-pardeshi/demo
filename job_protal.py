
import mysql.connector

my = mysql.connector.connect(host="localhost",user="root",password="mysql@123",database="job_portal2")

cursor = my.cursor()

insert = "insert into Seeker(username,password) values(%s,%s)"


#________________Student panel---------------------
        
##1. Register
##2. Login
##3. Search Jobs
##4. Apply for Job
##5. My Applications
##6. My Profile
##7. Logout

li = []
Student_details = []
Student_details2 = []
def Register():
    try:
        
        Username = input("\nEnter Your UserName:--")
        Password = input("\nEnter your password:--")
        insert = "insert into seeker(username,password) values(%s,%s)"
        values = {
            (Username,Password)
            }
        cursor.executemany(insert,values)
        my.commit()
        Student_Name = input("\nEnter Your Name:-")
        Student_College_Name = input("\nEnter Your College Name:-")
        Student_Mobile = input("\nEnter Your Are Mobile Number:-")
        Student_age = input("\nEnter your age:-")

        if len(Username)==0 or len(Password)==0 or len(Student_Mobile)==0 or len(Student_age)==0:
            print("Empty Field")
        else:
            li.append(Username)
            li.append(Password)
            Student_details.append(Student_Name)
            Student_details.append(Student_College_Name)
            Student_details.append(Student_Mobile)
            Student_details.append(Student_age)
            Student_details.append(Username)
            
            print("\nRegister Successfully")
            Student_details2.append(Student_details)

    except ValueError:
        print("Please Enter Currect value")

def Login():

    try:
        Username1 = input("\nEnter your Username")
        Password1 = input("\nEnter Your Password")
        select_Seenker = "select * from seeker where username=%s and password=%s"
        values =(Username1,Password1)
            
        cursor.execute(select_Seenker,values)
        res = cursor.fetchone()
        if len(Username1)==0 or len(Password1)==0:
            print("Empty Field")

        elif res!=None:
            print("Welcome To Job Portal")
            while True:
                print("\n1. Apply for Job\n2. My Applications\n3. My Profile\n4. Logout")
                choice2 = int(input("\n Enter Your Choice :--"))
                match(choice2):
                    case 1:
                        Apply_For_Job()
                    case 2:
                        My_Applications()
                    case 3:
                        My_Profile()
                    case 4:
                        print("Thank You....!!")
                        break
                    case _:
                        print("\nInvalid Choice")
        else:
            print("Go Register First")

    except ValueError:
        print("please enter currect value")


##Login()
##Register()
##Login()

##
##res = list(map(lambda x:x[2],Recruiter_List ))
##
##print(res)
list1 = []
list2_recuriter=[]
list3_recuriter = []

##Recuiter_Job_List = list(map(lambda x:x[2],Recruiter_List))
def Search_Job():
    Recuiter_Job_List = list(map(lambda x:x[2],Recruiter_List))
    print(Recuiter_Job_List)
    User = input("\nEnter your Job Title:-")

    if User not in Recuiter_Job_List:
        print("*Not Found Match*")

    else:
        for i in range(0,len(Recruiter_List),1):
            if User in  Recruiter_List[i][2]:
                print(f"\n{Recruiter_List[i]}\n")
                
                
            
##Search_Job()   

def My_Applications():

    print("This JOD you Priviously Search")
    for i in list1:
        print("Company Name :-",i[1],"Job Title :-",i[2],"Job Location :-",i[3],"Salary :-",i[4],"Experience :-",i[5])


##Last_Job_Search()


def Apply_For_Job():
    Recuiter_Job_List = list(map(lambda x:x[2],Recruiter_List))
    print(Recuiter_Job_List)

    User = input("\nEnter your Job Title:-")

    if User not in Recuiter_Job_List:
        print("*Not Found Match*")

    else:
        for i in range(0,len(Recruiter_List),1):
            if User in  Recruiter_List[i][2]:
                print(f"\n{Recruiter_List[i]}\n")
                Student_Name = input("\nEnter Your Name:-")
                Student_Mobile = input("\nEnter Your Are Mobile Number:-")
                list2_recuriter.append(Student_Name)
                list2_recuriter.append(Student_Mobile)
                list2_recuriter.append(Recruiter_List[i][2])
                list2_recuriter.append(Recruiter_List[i][3])
                list1.append(Recruiter_List[i])
        list3_recuriter.append(list2_recuriter)
    print("Applied Seccessfully")
    
##Apply_For_Job()   

def My_Profile():
    
    for i in range(0,len(Student_details2),1):
        print("\n Name :- ",Student_details2[i][0],"\n College Name:- ",Student_details2[i][1],"\n Mobile :- ",Student_details2[i][2],"\n Age:- ",Student_details2[i][3],"\n UserName :- ",Student_details2[i][4])


##====== RECRUITER ======
##
##1. Register
##2. Login
##3. Post Job
##4. Manage Jobs
##5. View Applicants
##6. Shortlist Candidate
##7. Logout

li2 = []
def Recruiter_Register():
    try:
        
        Username = input("\nEnter Your Name:--")
        Password = input("\nEnter your password:--")
        
        if len(Username)==0 or len(Password)==0:
            print("Empty Field")
        else:
            
            li2.append(Username)
            li2.append(Password)
            insert = "insert into  recuriter(username,password) values(%s,%s)"
            values = {
             (Username,Password)
            }
            cursor.executemany(insert,values)
            my.commit()
            
            print("\nRegister Successfully")

    except ValueError:
        print("Please Enter Currect value")


def Recruiter_Login():
    try:
        Username1 = input("\nEnter your Username :--")
        Password1 = input("\nEnter Your Password :--")
        select_data = "select * from recuriter where username=%s and password=%s"
        values = (Username1,Password1)
        cursor.execute(select_data,values)
        res1 = cursor.fetchone()
        
        if len(Username1)==0 or len(Password1)==0:
            print("Empty Field")
        elif res1!=None:
            print("\nWelcome To Job Portal")
            while True:
                print("\n1. Post Job\n2. Manage Jobs\n3. View Applicants\n4. Shortlist Candidate\n5. View Shortlist Candidate\n6. Logout")
                choice4 = int(input("\nEnter Your Choice:--"))
                match(choice4):
                    case 1:
                        Post_job()
                    case 2:
                        Manage_Job()
                    case 3:
                        view_Applicants()
                    case 4:
                        Shortlisted_candidate()
                    case 5:
                        View_Shortlisted_candidate()
                    case 6:
                        print("Thank You....!!")
                        break
        else:
            print("\nGo Register First")
                

    except ValueError:
        print("please enter currect value")
        
    
Recruiter_List = [
    [101, "TCS", "Python Developer", "Pune", 500000,"Python SQL OOP", "Fresher"],
    [102, "Infosys", "Data Analyst", "Bangalore", 600000, "Python  SQL  Excel", "Fresher"],
    [103, "Wipro", "Software Developer", "Mumbai", 550000, "Python  C++  DSA", "Fresher"]
]
list_For_Job = []

def Post_job():
    try:
        Company_Id = int(input("\nEnter Company ID :-"))
        Company_Name = input("\nEnter Company Name :-").capitalize()
        Post_Name = input("\nEnter Job Title :- ").capitalize()
        Job_Location = input("\nEnter Job Location :- ").capitalize()
        Job_Salary = input("\nEnter Job Salary :- ")
        Jod_skills = input("\nEnter Job Required Skills :- ").capitalize()
        Job_Expect = input("\nEnter Job For Fresher/Experienced").capitalize()

        insert = "insert into job_post(company_id,company_name,job_position,job_location,salary) values(%s,%s,%s,%s,%s,%s)"

        values = (Company_Id,Company_Name,Post_Name,Job_Location,Job_Salary)
        cursor.execute(insert,values)
        my.commit()

        list_For_Job.append(Company_Id)
        list_For_Job.append(Company_Name)
        list_For_Job.append(Post_Name)
        list_For_Job.append(Job_Location)
        list_For_Job.append(Job_Salary)
        list_For_Job.append(Jod_skills)
        list_For_Job.append(Job_Expect)

        Recruiter_List.append(list_For_Job)
        print(Recruiter_List)
        print("Job Added Successfully")

    except Exception:
        print("Invalid Value")
        
##Post_job()       
        
        

def Manage_Job():
    print("\nWhich Section You Modify:- 1.Company Name 2.Post Name 3.Job Location 4.Job Salary 5.Job Skills 6.jOB Exprience")
    check_it = list(map(lambda x:x[0],Recruiter_List))
    user = int(input("Enter Your Company Id :-"))


    if user not in check_it:
        print("Invalid Company Id")
    else:
        for i in range(0,len(Recruiter_List),1):
            if user == Recruiter_List[i][0]:
                user_index = int(input("\nEnter Which section You Modify :- "))
                user_change = input("\n Enter the Change :- ").capitalize()
                Recruiter_List[i][user_index]=user_change

                print(Recruiter_List)

    print("Modify Successfully")
    
def view_Applicants():
    for i in range(0,len(list3_recuriter),1):
        print("\n1. Applicants Name :-",list3_recuriter[i][0],"\n2. Applicants Contact Number :-",list3_recuriter[i][1],"\n3. Applicants applied postion :-",list3_recuriter[i][2])
        
##view_Applicants()

list_Shortlisted_candidate=[]
list_Shortlisted_candidate1=[]
def Shortlisted_candidate():
    list3_recuriter1 = list(map(lambda x:x[0],list3_recuriter))
    Candidate_Name = input("\nEnter Shortlisted candidate Name:-- ")

    if Candidate_Name not in list3_recuriter1:
        print("Sorry this Name candidate not present")
    else:
        for i in range(0,len(list3_recuriter),1):
            list_Shortlisted_candidate.append("Shortlisted")
            list_Shortlisted_candidate.append(list3_recuriter[i][0])
            list_Shortlisted_candidate.append(list3_recuriter[i][1])
            list_Shortlisted_candidate.append(list3_recuriter[i][2])
        list_Shortlisted_candidate1.append(list_Shortlisted_candidate)

##Shortlisted_candidate()
           
def View_Shortlisted_candidate():
    for i in range(0,len(list_Shortlisted_candidate1),1):
        if "Shortlisted" in list_Shortlisted_candidate1[i][0]:
            print("This condidate are selected:==\n",list_Shortlisted_candidate1[i])
    
##View_Shortlisted_candidate()       


def LogtOut():
    print("Thank For Use over application")
##    break



##====== RECRUITER ======
##
##1. Register
##2. Login
##3. Post Job
##4. Manage Jobs
##5. View Applicants
##6. Shortlist Candidate
##7. Logout

##=================================
##       JOB PORTAL SYSTEM
##=================================
##
##1. Job Seeker
##2. Recruiter
##3. Admin
##4. Exit
##
##Enter choice:

##1. Register
##2. Login
##3. Search Jobs
##4. Apply for Job
##5. My Applications
##6. My Profile
##7. Logout




##========== ADMIN PANEL ==========
##
##1. View All Job Seekers
##2. View All Recruiters
##3. View All Jobs


def Admin_Register():
    try:
        Admin_Name = input("\nEnter Your Name:--")
        Username = input("\nEnter your Username :--")
        Password = input("\nEnter Your Password :--")

        if len(Username)==0 or len(Password)==0:
            print("Empty Field")
        else:
            insert_Admin = "insert into admin(username,password) values(%s,%s)"
            values = {
                (Username,Password)
                }
            cursor.executemany(insert_Admin,values)
            my.commit()
            print("\nRegister Successfully")

    except ValueError:
        print("\n Enter curect value")
    
def Admin_Login():
    try:
        Username = input("\nEnter Your Username :--")
        Password = input("\nEnter Your Password :--")

        select_Admin = "select * from admin where username=%s and password=%s"
        values = (Username,Password)
        
        cursor.execute(select_Admin,values)
        res = cursor.fetchone()

        if res!=None:
            while True:
                print("\n1. View All Job_Seekers\n2. View All Recruiters\n3. View All Jobs\n4. Remove Recuriter\n5. Logout")
                choice5 = int(input("Enter your choice:--"))
                match(choice5):
                    case 1:
                        View_All_Job_Seekers()
                    case 2:
                        View_All_Recruiters()
                    case 3:
                        View_All_Jobs()
                    case 4:
                        Remove_Recuriter()
                    case 5:
                        print("\nThank for Use this portal")
                        break
                    case _:
                        print("\nInvalid Choice")
        else:
            print("\nGo Register First")
            
    except ValueError:
        print("\nEnter curect value")
    


def View_All_Job_Seekers():
    select_data = "select * from seeker"
    cursor.execute(select_data)
    res = cursor.fetchall()
    
    for i in res:
        print("\n Name:--",i[1],"*------------*Seeker Login Date and Time",i[3])

def View_All_Recruiters():
    select_data_for_recuriter = "select * from recuriter"
    cursor.execute(select_data_for_recuriter)
    res1 = cursor.fetchall()
    
    for i in res1:
        print("\n UserName:--",i[1],"*------------*Recruiters Login date and time:--",i[3])
        
def Remove_Recuriter():
    user_name = input("\nEnter Recuriter name to you remove from portal:--")
    delete = "delete from recuriter where username = %s"
    values = {
        (user_name,)
        }
    cursor.executemany(delete,values)
    my.commit()

    print("\nRecuriter Remove Successfullu..!!")

def View_All_Jobs():
    print("\nTotal available Jobs")
    for i in Recruiter_List:
        print("\n", i)





while True:
    print("\n*======(HireX)======================================================================================*")
    print("\n==================(HireX)================*JOB PORTAL SYSTEM*==================(HireX)================")
    print("\n*======================================================================================(HireX)======*")
    print("\n1. Job Seeker\n2. Recruiter\n3. Admin\n4. Exit")
    choice = int(input("\nEnter your choice :--"))
    match(choice):
        case 1:
            while True:
                print("\n1. Register\n2. Login\n3. Search Jobs\n4. Exit")
                choice1 = int(input("Enter Seeker choice"))
                match(choice1):
                    case 1:
                        Register()
                    case 2:
                        Login()
                    case 3:
                        Search_Job()
                    case 4:
                        print("\nThank You....!!")
                        break  
        case 2:
            while True:
                print("\n1. Register\n2. Login\n3. Exit")
                choice3 = int(input("Enter your choice:--"))
                match(choice3):
                    case 1:
                        Recruiter_Register()

                    case 2:
                        Recruiter_Login()
                        
                    case 3:
                        print("\nThank You....!!")
                        break

        case 3:
            while True:
                print("\n1. Register\n2. Login\n3. Exit")
                choice6 = int(input("Enter Your Choice"))
                match(choice6):
                    case 1:
                        Admin_Register()
                    case 2:
                        Admin_Login()
                    case 3:
                        print("\n Thank You....!!")
                        break

        case 4:
            print("\n Thank For use this Application")
            break

           

























