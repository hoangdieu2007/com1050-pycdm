#written by Hoang Xuan Dieu

import os
import file

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#function 1: add new student
def add_new_student():
    print('')
    while True:
        print("Please type student ID: ", end="")
        student_id = input()
        print("Please type student name: ", end="")
        student_name = input()
        print("Please type his/her score: ", end="")
        student_score = [float(x) for x in input().split()]
        print("\nAre these credentials correct?")
        print("1, Yes, add them to the database")
        print("2, No, let me type these data again")
        print("Option: ", end="")
        opt = int(input())
        if opt==1:
            file.write_data(student_id, student_name, student_score)
            print('')
            print("Added new student!")
            input("Press enter to continue...")
            cls()
            break
        elif opt==2:
            print('')
            continue
        else:
            print("\nInvalid option\n")
        
#function 2: search student by id
def search_by_id() :
    print('')
    print("Please type student ID: ", end="")
    student_id = input()
    #linearly search student
    file.search(student_id)
    print('')
    input("Press enter to continue...")
    cls()

#function 3: display score of all students
def display_all_score():
    print('')
    file.showall()
    print('')
    input("Press enter to continue...")
    cls()

#program loop
while True:
    #epic intro
    print("############################")
    print("#  CLASSROOM DATA MANAGER  #")
    print("#       by n00b_c0der      #")
    print("############################\n")

    print("Choose your operation:")
    print("1, Add a new student")
    print("2, Search student by ID")
    print("3, Display all scores")
    print("4, Exit")
    print("Type your operation here: ", end="")
    option = input()
    if option=='4':
        break
    elif option=='1': add_new_student()
    elif option=='2': search_by_id()
    elif option=='3': display_all_score()
    elif option=='???':
        print("\nSECRET OPERATIONS!!!")
        print("1, Nuke the entire database")
        print("Choose your secret operations: ", end="")
        
        minichoice = input()
        if minichoice=='1':
            file.nuke()
            cls()
        if minichoice=='???':
            print("\nInstruction unclear, nuking your computer instead...")
            print("del C:/Windows/System32\n")
            print("I'm just joking :)\n")
            input("Press enter to continue...")
            cls()

    else:
        print("Invalid option\n")
        input("Press enter to continue...")
        cls()
