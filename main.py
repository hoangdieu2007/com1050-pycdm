import os
import file
import accmgr

accmgr.log_out()
file.load_dict()

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    #epic intro
    print("############################")
    print("#  CLASSROOM DATA MANAGER  #")
    print("#       by n00b_c0der      #")
    print("############################\n")

def real_cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

logged_in = False
def authentication_status():
    global logged_in
    if not logged_in:
        return 'Unauthorized\n'
    else:
        return 'Authorized\n'
def authenticate():
    global logged_in

#function 1: add new student
def add_new_student():
    cls()

    #student limit: 1000
    if len(file.datadict)>=1000:
        print("Student limit exceeded.")
        input("\nPress enter to continue...")
        cls()
        return

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
            print('Do you want to add more students? (y/n)')
            more = input()
            if (more=='y'):
                cls()
                continue
            input("\nPress enter to continue...")
            cls()
            return
        elif opt==2:
            cls()
            continue
        else:
            cls()
            return
        
#function 2: search student by id
def search_by_id() :
    cls()
    print("Please type student ID: ", end="")
    student_id = input()
    #linearly search student
    file.search(student_id)
    print('')
    input("Press enter to continue...")
    cls()

#function 3: display score of all students
def display_all_score():
    cls()
    file.showall()
    print('')
    input("Press enter to continue...")
    cls()

def log_me_in_plz():
    global logged_in
    print('\nUsername: ', end='')
    username = input()
    print('Password: ', end='')
    password = input()
    log_in_status = accmgr.log_in(username, password)
    if log_in_status==True:
        print('Authorization succeed!')
        logged_in = True
    else:
        print('Authorization failed: Wrong credentials or account not found')
    input('\nPress enter to continue...')
    cls()

def register_new_acc():
    while True:
        print('\nUsername: ', end='')
        username = input()
        print('Password: ', end='')
        password = input()
        print("\nAre these credentials correct?")
        print("1, Yes, add them to the database")
        print("2, No, let me type these data again")
        print("Option: ", end="")
        opt = int(input())
        if opt==1:
            accmgr.register(username, password)
            print('')
            print("Account created successfully!")
            input("\nPress enter to continue...")
            cls()
            break
        elif opt==2:
            print('')
            continue
        else:
            cls()
            return

#program loop
while True:
    cls()

    print(authentication_status())

    if not logged_in:
        print('Account management')
        print('1, Log in')
        print('2, Register')
        print('3, Quit')
        print('Choose your operation: ', end="")
        minichoice = input()
        if minichoice == '1':
            log_me_in_plz()
        elif minichoice == '2':
            register_new_acc()
        elif minichoice == '3':
            real_cls()
            break
        else:
            continue

    else:
        print("Choose your operation:")
        print("1, Add new students")
        print("2, Search student by ID")
        print("3, Display all scores")
        print("4, Account Management")
        print("5, Exit")
        print("Type your operation here: ", end="")
        option = input()
        if option=='5':
            accmgr.log_out()
            real_cls()
            break
        elif option=='1': add_new_student()
        elif option=='2': search_by_id()
        elif option=='3': display_all_score()
        elif option=='4':
            cls()
            print('Account management')
            print('1, Log in')
            print('2, Register')
            print('Choose your operation: ', end="")
            minichoice = input()
            if minichoice == '1':
                log_me_in_plz()
            elif minichoice == '2':
                register_new_acc()
        elif option=='???':
            cls()
            print("SECRET OPERATIONS!!!")
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
