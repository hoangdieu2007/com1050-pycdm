import os
import file
import accmgr

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

#function 1: add new student
def add_new_student():
    cls()

    while True:
        print("Please type student ID: ", end="")
        student_id = input()
        print("Please type student name: ", end="")
        student_name = input()
        print("Please type his/her regular assessment scores: ", end="")
        student_ra_score = [float(x) for x in input().split()]
        print("Please type his/her midterm scores: ", end="")
        student_mt_score = [float(x) for x in input().split()]
        print("Please type his/her final term score: ", end="")
        student_ft_score = [float(x) for x in input().split()]
        print("\nAre these credentials correct?")
        print("1, Yes, add them to the database")
        print("2, No, let me type these data again")
        print("Option: ", end="")
        opt = int(input())
        if opt==1:
            status = file.write_data(student_id, student_name, student_ra_score, student_mt_score, student_ft_score)
            print('')
            print(status)
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

#f4: calculate gpa based on id
def calc_gpa_by_id():
    cls()
    print("Please type student ID: ", end="")
    student_id = input()
    file.gpa_check(student_id)
    print('')
    input("Press enter to continue...")
    cls()

#f5: edit score of an id
def edit_score_by_id():
    cls()
    print("Please type student ID: ", end="")
    student_id = input()
    file.grade_edit(student_id)
    print('')
    input("Press enter to continue...")
    cls()

#f6: remove by id
def remove_by_id():
    cls()
    print("Please type student ID: ", end="")
    student_id = input()
    file.remove(student_id)
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

def log_me_out_plz():
    global logged_in
    accmgr.log_out()
    logged_in = False
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
        
def change_password():
    cls()
    print("Type new password: ", end='')
    new_password = input()
    print("Are you sure you want to change to this password? (Yes/No) ", end='')
    choice = input()
    if choice.lower() == 'yes':
        accmgr.change_pass(new_password)
    cls()

#program loop

cls()
accmgr.log_out()
file.load_dict()

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
        print("4, Display GPA by ID")
        print("5, Edit student's score by ID")
        print("6, Remove student from database by ID")
        print("S, Save changes")
        print("A, Account Management")
        print("X, Advanced Operations")
        print("E, Exit")
        print("Type your operation here: ", end="")
        option = input()
        if option.upper()=='E':
            file.save_dict()
            accmgr.log_out()
            real_cls()
            break
        elif option=='1': add_new_student()
        elif option=='2': search_by_id()
        elif option=='3': display_all_score()
        elif option=='4': calc_gpa_by_id()
        elif option=='5': edit_score_by_id()
        elif option=='6': remove_by_id()
        elif option.upper()=='S':
            file.save_dict()
            cls()
        elif option.upper()=='A':
            cls()
            print('Account management')
            print('1, Log out')
            print('2, Change password')
            print('Choose your operation: ', end="")
            minichoice = input()
            if minichoice == '1':
                log_me_out_plz()
            elif minichoice == '2':
                change_password()
        elif option.upper()=='X':
            cls()
            print("ADVANCED OPERATIONS!!!")
            print("1, Nuke the entire database")
            print("Choose your operation: ", end="")
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
