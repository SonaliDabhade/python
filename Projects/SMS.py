import time

Students = {}
id = 1000


def addStudent():
    global id
    id+=1
    Students[id]={}

    Students[id]["name"] = input("Enter Your Name:")
    Students[id]["marks"] = float(input("Enter Your Marks:"))
    print("Student Added Successfully")

def updateStudent():
    id = int(input("Please Enter Student Id :"))
    print("1) Update Name ")
    print("2) Update Marks ")
    print("3) Cancel Update ")

    option = int(input("Enter Your Choice : "))
    if option == 1:
        Students[id]["name"] = input("Enter Your Name:")
        print("Name Updated Successfully")
    elif option == 2:
        Students[id]["marks"] = float(input("Enter Your Marks:"))
        print("Marks Updated Successfully")
    elif option == 3:
        print("Update Operation Cancelled.....")
    else:
        print("Invalid Choice Please Try Again")
    
def deleteStudent():
    id = int(input("Please Enter Student Id :"))
    print("Are You Sure To Delete Student Name ",Students[id]["name"]," ? ")
    print("1)Yes")
    print("3)No")


    option = int(input("Enter Your Choice : "))
    if option == 1:
        name = Students[id]["name"]
        del Students[id]
        print("Student With Name ",name," Deleted Successfully")
    elif option == 2:
        print("Delete Operation Cancelled....")
    else:
        print("Invalid Choice Please Try Again")
    
def viewStudents():
    if(len(Students)==0):
        print("Please Add Some Student List is Empty...")
    else:
        print("--------------------Students Details--------------------")
        for i in Students:
            print("ID :",i)
            print("Name : ",Students[i]["name"])
            print("Marks : ",Students[i]["marks"])
            print("----------------------------------------")




print("------------------------Student Management System------------------------")
print()
time.sleep(1)
print("                   Welcome to Student Management System                   ")
print()
time.sleep(1)
print("            Please Select Which Operation you want to perform            ")
time.sleep(1)





while True:
    print("1) Add New Student")
    print("2) Update New Student ")
    print("3) Delete New Student ")
    print("4) View Students ")
    print("5) Exit ")
    option = int(input("Enter Your Choice : "))

    if option == 1:
        addStudent()
    elif option == 2:
        updateStudent()
    elif option == 3:
        deleteStudent()
    elif option == 4:
        viewStudents()
    elif option ==5:
        print("------------------------Thank You for using------------------------")
        time.sleep(1)
        break
    else:
        print("Invalid Choice Please Try Again...")

