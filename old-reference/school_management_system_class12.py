# COMPUTER SCIENCE PROJECT - SCHOOL MANAGEMENT SYSTEM

# Original academic project: Class XII Computer Science
# Academic Year: 2023-24
# Author: Anish Agarwal
#
# This file is preserved as an archival reference version.
# It is not the current production/web implementation.



# Importing the required module for MySQL database connection with Python and aliasing it as 'CON' for ease of use
import mysql.connector as CON
import os

# Establishing a connection to the MySQL server.
# Set DB_USER and DB_PASSWORD in your environment before running.
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")
OBJ = CON.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)

# Creating a cursor object for executing MySQL queries
CUR = OBJ.cursor()

# Creating the database 'school' if it does not exist
CUR.execute('CREATE DATABASE IF NOT EXISTS school')
CUR.execute('USE school')

# Creating the tables if they do not exist
CUR.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        Name VARCHAR(20),
        Class VARCHAR(10),
        Roll_no VARCHAR(10) PRIMARY KEY,
        Address VARCHAR(50),
        Phone VARCHAR(10) ) ''')

CUR.execute('''
    CREATE TABLE IF NOT EXISTS Teacher (
        Teacher_Code VARCHAR(10) PRIMARY KEY,
        Name VARCHAR(20),
        Salary VARCHAR(10),
        Address VARCHAR(50),
        Phone VARCHAR(10) ) ''')

CUR.execute('''
    CREATE TABLE IF NOT EXISTS Class_Attendance (
        Class VARCHAR(10),
        Class_Teacher VARCHAR(20),
        Strength VARCHAR(5),
        Date VARCHAR(10),
        Absentees VARCHAR(5) ) ''')

CUR.execute('''
    CREATE TABLE IF NOT EXISTS Teacher_Attendance (
        Name VARCHAR(20),
        Date VARCHAR(10),
        Attendance VARCHAR(10) ) ''')

CUR.execute('''
    CREATE TABLE IF NOT EXISTS Fee_Structure (
        Class VARCHAR(10),
        School_Fee VARCHAR(10),
        Bus_Fee VARCHAR(10),
        Excursion_Fee VARCHAR(10),
        Tech_Fee VARCHAR(10),
        Total_Fee VARCHAR(10) ) ''')

CUR.execute('''
    CREATE TABLE IF NOT EXISTS Library (
        Book_ID VARCHAR(10),
        Title VARCHAR(30),
        Author VARCHAR(20),
        Publisher VARCHAR(20),
        Genre VARCHAR(20) ) ''')

# Function for adding Student Details Record
def Add_Student_Rec():
    Name = input("Enter Student name : ")
    Class = input("Enter Class : ")
    Roll_no = int(input("Enter Roll no : "))
    Address = input("Enter Address : ")
    Phone = input("Enter Phone number : ")
    DATA = (Name, Class, Roll_no, Address, Phone)
    SQL = 'insert into Student values(%s,%s,%s,%s,%s)'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data entered successfully")
    print()

# Function for removing Student Details Record
def Remove_Student_Rec():
    Class = input("Enter Class : ")
    Roll_no = int(input("Enter Roll no : "))
    DATA = (Class, Roll_no)
    SQL = 'delete from Student where Class=%s and Roll_no=%s'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data removed successfully")
    print()

# Function for updating Student Details Record
def Update_Student_Rec():
    Name = input("Enter Student name : ")
    Class = input("Enter Class : ")
    Roll_no = int(input("Enter Roll no : "))
    Address = input("Enter updated Address : ")
    Phone = input("Enter updated Phone number : ")
    DATA = (Address, Phone, Name, Class, Roll_no)
    SQL = 'Update Student set Address=%s, Phone=%s where Name=%s and (Class=%s and Roll_no=%s)'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data updated successfully")
    print()

# Function for displaying Student Detail Records
def Display_Student_Rec():
    Class = input("Enter Class : ")
    DATA = (Class, )
    SQL = 'select * from Student where Class=%s'
    CUR.execute(SQL, DATA)
    Data = CUR.fetchall()
    for i in Data:
        print(f"Name : {i[0]}")
        print(f"Class : {i[1]}")
        print(f"Roll Number : {i[2]}")
        print(f"Address : {i[3]}")
        print(f"Phone : {i[4]}")
        print()
    print()



# Function for adding Teacher Details Record
def Add_Teacher_Rec():
    Teacher_Code = int(input("Enter Teacher Code : "))
    Name = input("Enter Teacher name : ")
    Salary = int(input("Enter salary : "))
    Address = input("Enter address : ")
    Phone = input("Enter Phone number : ")
    DATA = (Teacher_Code, Name, Salary, Address, Phone)
    SQL = 'insert into Teacher values(%s,%s,%s,%s,%s)'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data entered successfully")
    print()

# Function for removing Teacher Details Record
def Remove_Teacher_Rec():
    Name = input("Enter Teacher name : ")
    Teacher_Code = int(input("Enter Teacher Code : "))
    DATA = (Name, Teacher_Code)
    SQL = 'delete from Teacher where Name=%s and Teacher_Code=%s'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data removed successfully")
    print()

# Function for updating Teacher Salary Record
def Update_Salary():
    Name = input("Enter Teacher name : ")
    Teacher_Code = int(input("Enter Teacher Code : "))
    Salary = int(input("Enter updated Salary : "))
    DATA = (Salary, Name, Teacher_Code)
    SQL = 'update Teacher set Salary=%s where Name=%s and Teacher_Code=%s'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data updated successfully")
    print()

# Function for displaying Teacher Detail Records
def Display_Teacher_Records():
    SQL = 'select * from Teacher'
    CUR.execute(SQL)
    Data = CUR.fetchall()
    for i in Data:
        print(f"Teacher Code : {i[0]}")
        print(f"Name : {i[1]}")
        print(f"Salary : {i[2]}")
        print(f"Address : {i[3]}")
        print(f"Phone : {i[4]}")
        print()
    print()



# Function for adding Class Attendance Record
def Add_Class_Attendance_Rec():
    Class = input("Enter Class : ")
    Class_Teacher = input("Enter Class teacher name : ")
    Strength = int(input("Enter Class strength : "))
    Date = input("Enter Date : ")
    Absentees = int(input("Enter Number of absentees : "))
    DATA = (Class, Class_Teacher, Strength, Date, Absentees)
    SQL = 'insert into Class_Attendance values(%s,%s,%s,%s,%s)'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data entered successfully")
    print()

# Function for displaying Class Attendance Records
def Display_Class_Attendance():
    SQL = 'select * from Class_Attendance'
    CUR.execute(SQL)
    Data = CUR.fetchall()
    for i in Data:
        print(f"Class : {i[0]}")
        print(f"Class teacher : {i[1]}")
        print(f"Total Strength : {i[2]}")
        print(f"Date : {i[3]}")
        print(f"Absentees : {i[4]}")
        print()
    print()



# Function for adding Teacher Attendance Record
def Add_Teacher_Attendance_Rec():
    Name = input("Enter Teacher name : ")
    Date = input("Enter Date : ")
    Attendance = input("Enter Attendance : ")
    DATA = (Name, Date, Attendance)
    SQL = 'insert into Teacher_Attendance values(%s,%s,%s)'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data entered successfully")
    print()
    
# Function for displaying Teacher Attendance Records
def Display_Teacher_Attendance():
    SQL = 'select * from Teacher_Attendance'
    CUR.execute(SQL)
    Data = CUR.fetchall()
    for i in Data:
        print(f"Name : {i[0]}")
        print(f"Date : {i[1]}")
        print(f"Attendance : {i[2]}")
        print()
    print()


# Function for adding Fee Structure Record
def Insert_Fees():
    Class = input("Enter Class : ")
    School_Fee = int(input("Enter School fee : "))
    Bus_Fee = int(input("Enter Bus fee : "))
    Excursion_Fee = int(input("Enter Excursion fee : "))
    Tech_Fee = int(input("Enter Tech fee : "))
    Total_Fee = School_Fee + Bus_Fee + Excursion_Fee + Tech_Fee
    DATA = (Class, School_Fee, Bus_Fee, Excursion_Fee, Tech_Fee, Total_Fee)
    SQL = 'insert into Fee_Structure values (%s,%s,%s,%s,%s,%s)'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data entered successfully")
    print()

# Function for removing Fee Structure Record
def Remove_Fees():
    Class = input("Enter Class : ")
    DATA = (Class, )
    SQL = 'delete from Fee_Structure where Class=%s'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data removed successfully")
    print()

# Function for updating Fee Structure Record
def Update_Fees():
    Class = input("Enter Class : ")
    School_Fee = int(input("Enter updated School fee : "))
    Bus_Fee = int(input("Enter updated Bus fee : "))
    Excursion_Fee = int(input("Enter updated Excursion fee : "))
    Tech_Fee = int(input("Enter updated Tech fee : "))
    Total_Fee = School_Fee + Bus_Fee + Excursion_Fee + Tech_Fee
    DATA = (School_Fee, Bus_Fee, Excursion_Fee, Tech_Fee, Total_Fee, Class)
    SQL = 'update Fee_Structure set School_Fee=%s, Bus_Fee=%s, Excursion_Fee=%s, Tech_Fee=%s, Total_Fee=%s where Class=%s'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data updated successfully")
    print()
    
# Function for displaying Fee Structure Records
def Display_Fees():
    Class = input("Enter Class : ")
    DATA = (Class, )
    SQL = 'select * from Fee_Structure where Class=%s'
    CUR.execute(SQL, DATA)
    Data = CUR.fetchall()
    for i in Data:
        print(f"Class : {i[0]}")
        print(f"School Fee : {i[1]}")
        print(f"Bus Fee : {i[2]}")
        print(f"Excursion Fee : {i[3]}")
        print(f"Tech Fee : {i[4]}")
        print(f"Total Fee : {i[5]}")
        print()
    print()



# Function for adding Record of Book to Library
def Add_Book():
    Book_ID = int(input("Enter Book ID : "))
    Title = input("Enter Book Title : ")
    Author = input("Enter name of Author : ")
    Publisher = input("Enter Publisher name : ")
    Genre = input("Enter Genre of the book : ")
    DATA = (Book_ID, Title, Author, Publisher, Genre)
    SQL = 'insert into Library values(%s,%s,%s,%s,%s)'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data entered successfully")
    print()

# Function for removing Record of Book from Library
def Remove_Book():
    Title = input("Enter Book Title : ")
    Book_ID = int(input("Enter Book ID : "))
    DATA = (Title, Book_ID)
    SQL = 'delete from Library where Title=%s and Book_ID=%s'
    CUR.execute(SQL, DATA)
    OBJ.commit()
    print("Data removed successfully")
    print()

# Function for displaying Records of Books in Library
def Display_Books():
    SQL = 'select * from Library'
    CUR.execute(SQL)
    Data = CUR.fetchall()
    for i in Data:
        print(f"Book ID : {i[0]}")
        print(f"Title : {i[1]}")
        print(f"Author : {i[2]}")
        print(f"Publisher : {i[3]}")
        print(f"Genre : {i[4]}")
        print()
    print()



# Defining the MENU() function to interact with user
def MENU():
    while True:
        print("""
****************************** MAIN MENU *****************************

1. Student Portal
2. Teacher Portal
3. Class Attendance Portal
4. Teacher Attendance Portal
5. Fee Structure Portal
6. Library Portal
7. Exit School Management System
""")
        Choice = int(input("Enter the Serial Number of the Portal you want to Access : "))
        print()

        if Choice == 1:
            while True:
                print("1. Add Student Record")
                print("2. Remove Student Record")
                print("3. Update Student Record")
                print("4. Display Student Records")
                print("5. Exit Student Portal")
                print()
                Task = int(input("Enter Serial Number of Desired Task : "))
                if Task == 1:
                    Add_Student_Rec()
                elif Task == 2:
                    Remove_Student_Rec()
                elif Task == 3:
                    Update_Student_Rec()
                elif Task == 4:
                    Display_Student_Rec()
                elif Task == 5:
                    return
                else:
                    print("Invalid choice...Please enter a valid option !!!")

        elif Choice == 2:
            while True:
                print("1. Add Teacher Record")
                print("2. Remove Teacher Record")
                print("3. Update Teacher Salary")
                print("4. Display Teacher Records")
                print("5. Exit Teacher Portal")
                print()
                Task = int(input("Enter Serial Number of Desired Task : "))
                if Task == 1:
                    Add_Teacher_Rec()
                elif Task == 2:
                    Remove_Teacher_Rec()
                elif Task == 3:
                    Update_Salary()
                elif Task == 4:
                    Display_Teacher_Records()
                elif Task == 5:
                    return
                else:
                    print("Invalid choice...Please enter a valid option !!!")

        elif Choice == 3:
            while True:
                print("1. Add Class Attendance Record")
                print("2. Display Class Attendance Records")
                print("3. Exit Class Attendance Portal")
                print()
                Task = int(input("Enter Serial Number of Desired Task : "))
                if Task == 1:
                    Add_Class_Attendance_Rec()
                elif Task == 2:
                    Display_Class_Attendance()
                elif Task == 3:
                    return
                else:
                    print("Invalid choice...Please enter a valid option !!!")

        elif Choice == 4:
            while True:
                print("1. Add Teacher Attendance Record")
                print("2. Display Teacher Attendance Records")
                print("3. Exit Teacher Attendance Portal")
                print()
                Task = int(input("Enter Serial Number of Desired Task : "))
                if Task == 1:
                    Add_Teacher_Attendance_Rec()
                elif Task == 2:
                    Display_Teacher_Attendance()
                elif Task == 3:
                    return
                else:
                    print("Invalid choice...Please enter a valid option !!!")

        elif Choice == 5:
            while True:
                print("1. Add Fee Structure")
                print("2. Remove Fee Structure")
                print("3. Update Fee Structure")
                print("4. Display Fee Structure")
                print("5. Exit Fee Structure Portal")
                print()
                Task = int(input("Enter Serial Number of Desired Task : "))
                if Task == 1:
                    Insert_Fees()
                elif Task == 2:
                    Remove_Fees()
                elif Task == 3:
                    Update_Fees()
                elif Task == 4:
                    Display_Fees()
                elif Task == 5:
                    return
                else:
                    print("Invalid choice...Please enter a valid option !!!")

        elif Choice == 6:
            while True:
                print("1. Add Book to Library")
                print("2. Remove Book from Library")
                print("3. Display Books in Library")
                print("4. Exit Library Portal")
                print()
                Task = int(input("Enter Serial Number of Desired Task : "))
                if Task == 1:
                    Add_Book()
                elif Task == 2:
                    Remove_Book()
                elif Task == 3:
                    Display_Books()
                elif Task == 4:
                    return
                else:
                    print("Invalid choice...Please enter a valid option !!!")

        elif Choice == 7:                       # Exit the software if the user chooses to exit
            print('THANK YOU FOR USING SCHOOL MANAGEMENT SYSTEM !!!')
            print('Exiting the system !  Hoping to see you again !  Goodbye...')
            os._exit(0)
            
        else:
            print("Invalid choice...Please enter a valid option !!!")


# MAIN PROGRAM

print('''
----------------------------------------------------------------------
                 WELCOME TO NOVA PINNACLE HIGH SCHOOL
----------------------------------------------------------------------
''')

MENU()              # Calling the MENU() function to start the interaction with user
