import csv

fields = ['id', 'name', 'ra_score', 'mt_score', 'ft_score']
database = 'database.csv'
auth_status = 'auth_status.txt'
accounts = 'acc.csv'

#obsolete code, previously used for operating on csv files

def nuke():
    global database, fields, accounts
    with open(database, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
    with open(accounts, 'w') as file:
        file.write('')

def write_data_csv(id, name, ra_score, mt_score, ft_score):
    global database, fields
    with open(database, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writerow({'id':id, 'name':name, 'ra_score':ra_score, 'mt_score':mt_score, 'ft_score':ft_score})

def search_csv(id):
    global database, fields
    found = False
    with open(database, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == id:
                found = True
                break
    if not found:
        print("Student not found")
    else:
        print("Name: ", row['name'])
        print("Regular Assessment Score: ", row['ra_score'])
        print("Midterm Score: ", row['ra_score'])
        print("Final Exam Score: ", row['ra_score'])

def showall_csv():
    global database, fields
    with open(database, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("ID:", row['id'])
            print("Name: ", row['name'])
            print("Regular Assessment Score: ", row['ra_score'])
            print("Midterm Score: ", row['ra_score'])
            print("Final Exam Score: ", row['ra_score'])
            print('')

#dictionary processing

datadict = {}

def tolst(a):
    if type(a) is list:
        return a
    return eval(a)

def load_dict():
    global database, datadict
    try:
        with open(database, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                datadict[row['id']] = {'name' : row['name'], 'ra_score' : tolst(row['ra_score']), 'mt_score' : tolst(row['mt_score']), 'ft_score' : tolst(row['ft_score'])}
    except KeyError:
        print('Database file is corrupted. To continue using this program, all data must be wiped. Proceed?')
        print('Yes/No: ', end='')
        choice = input()
        if choice.lower() == 'yes':
            nuke()
            load_dict()
        else:
            quit()

def save_dict():
    global database, fields, datadict
    with open(database, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for id in datadict:
            writer.writerow({'id':id, 'name': datadict[id]['name'], 'ra_score' : datadict[id]['ra_score'], 'mt_score' : datadict[id]['mt_score'], 'ft_score' : datadict[id]['ft_score']})

def write_data(id, name, ra_score, mt_score, ft_score):
    global datadict
    if id in datadict:
        return 'Student already exist.'
    datadict[id] = {'name' : name, 'ra_score' : ra_score, 'mt_score':mt_score, 'ft_score':ft_score}
    return 'Added new student!'

def search(id):
    global datadict
    if id in datadict:
        print('Name:', datadict[id]['name'])
        print('Regular Assessment Score:', datadict[id]['ra_score'])
        print("Midterm Score:", datadict[id]['mt_score'])
        print("Final Exam Score:", datadict[id]['ft_score'])
    else:
        print('Student not found')

def remove(id):
    global datadict
    found = datadict.pop(id, False)
    if found == False:
        print("No student with this ID was found")
    else:
        print("Student removed")

def showall():
    global datadict
    for id in datadict:
        print('ID:', id)
        print('Name:', datadict[id]['name'])
        print('Regular Assessment Score:', datadict[id]['ra_score'])
        print('Midterm Score:', datadict[id]['mt_score'])
        print('Final Exam Score:', datadict[id]['ft_score'])
        print('')

#gpa

def gpa_check(id):
    global datadict

    if not id in datadict:
        print( 'Student not found.')
        return
    
    lst1 = datadict[id]['ra_score']
    lst2 = datadict[id]['mt_score']
    lst3 = datadict[id]['ft_score']

    if len(lst1) < 3 or len(lst2) < 2 or len(lst3) < 1:
        count = 0
        for v in lst1:
            count += v
        for n in lst2:
            count += n
        for m in lst3:
            count += m
        tbc = count / (len(lst1) + len(lst2) + len(lst3))
        if len(lst1) < 3:
            x = 3-len(lst1)
            lst1.extend([tbc]*x)
        if len(lst2) < 2:
            y = 2-len(lst2)
            lst2.extend([tbc]*y)
        if len(lst3) < 1:
            z = 1-len(lst3)
            lst3.extend([tbc]*z)
        count1 = 0
        count2 = 0
        count3 = 0
        for v in lst1:
            count1 += v
        for n in lst2:
            count2 += n
        for m in lst3:
            count3 += m
        Predicted_GPA = (count1/3)*(10/100) + (count2/2)*(30/100) + count3*(60/100)
        if Predicted_GPA >= 9.0:
            print(f"Estimated GPA: {Predicted_GPA}\nAcademic Performance: Excellent")
        elif 8.0 <= Predicted_GPA < 9.0:
            print(f"Estimated GPA: {Predicted_GPA}\nAcademic Performance: Very Good")
        elif 7.0 <= Predicted_GPA < 8.0:
            print(f"Estimated GPA: {Predicted_GPA}\nAcademic Performance: Good")
        elif 5.0 <= Predicted_GPA < 7.0:
            print(f"Estimated GPA: {Predicted_GPA}\nAcademic Performance: Average")
        else:
            print(f"Estimated GPA: {Predicted_GPA}\nAcademic Performance: Poor")
    elif len(lst1) > 3 or len(lst2) > 2 or len(lst3) > 1:
        print("Input Error.")
    elif len(lst1) == 3 and len(lst2) == 2 and len(lst3) == 1:
        normal_score = 0
        midterm_score = 0
        final_score = 0
        for v in lst1:
            normal_score += v
        for n in lst2:
            midterm_score += n
        final_score = lst3[0]
        GPA = ((normal_score/3)*(10/100) + (midterm_score/2)*(30/100) + final_score*(60/100))
        if GPA >= 9.0:
            print(f"GPA: {GPA}\nAcademic Performance: Excellent")
        elif 8.0 <= GPA < 9.0:
            print(f"GPA: {GPA}\nAcademic Performance: Very Good")
        elif 7.0 <= GPA < 8.0:
            print(f"GPA: {GPA}\nAcademic Performance: Good")
        elif 5.0 <= GPA < 7.0:
            print(f"GPA: {GPA}\nAcademic Performance: Average")
        else:
            print(f"GPA: {GPA}\nAcademic Performance: Poor")
    
#edit

def grade_edit(id):
    global datadict

    if not id in datadict:
        print( 'Student not found.')
        return
    
    d_thuong_xuyen = datadict[id]['ra_score']
    d_giua_ky = datadict[id]['mt_score']
    d_cuoi_ky = datadict[id]['ft_score']

    #debug
    #print(len(d_thuong_xuyen))

    print("--- CHOOSE TYPE OF GRADE TO EDIT ---")
    print("1. Regular Assessment Score")
    print("2. Midterm Score")
    print("3. Final Exam Score")
    
    loai = input("Type your choice (1-3):")
    
    d_hien_tai = None
    ten_loai = ""
    if loai == '1':
        d_hien_tai = d_thuong_xuyen
        ten_loai = "Regular Assessment"
    elif loai == '2':
        d_hien_tai = d_giua_ky
        ten_loai = "Midterm"
    elif loai == '3':
        d_hien_tai = d_cuoi_ky
        ten_loai = "Final Exam"
    else:
        print("Invalid Choice!")
        return

    print(f"\nOperating with: {ten_loai} Score")
    print(f"Current list: {d_hien_tai}")
    if d_hien_tai is d_cuoi_ky:
        new_score = input('New Score:')
        while new_score.isdigit() == False and new_score > 10:
            new_score = input('New Score:')
        new_score = float(new_score)
        d_hien_tai[0] = new_score
    else:
        print("\n--- CHOOSE EDIT MODE ---")
        print("1. Edit a specific score")
        print("2. Edit all scores")
        mode = input("Type your choice (1-2): ")

        if mode == '1':
            try:
            # Hiển thị cho người dùng từ 1 đến độ dài list
                vi_tri_nhap = int(input(f"Type the position of the score to edit (from 1 to {len(d_hien_tai)}): "))
                index_thuc = vi_tri_nhap - 1 
                if 0 <= index_thuc < len(d_hien_tai):
                    diem_moi = float(input(f"Type new score for position {vi_tri_nhap}: "))
                    while diem_moi > 10:
                        diem_moi = float(input('Please type a valid score:'))
                    d_hien_tai[index_thuc] = diem_moi
                else:
                    print(f"Error: Position {vi_tri_nhap} is not in range!")
            except ValueError:
                print("Error: Please input the correct data type.")

        elif mode == '2':
            smaller_equal_10 = False
            try:
                chuoi_nhap = input("Type all scores in one line, each separated by a space: ")
                list_moi = [float(x) for x in chuoi_nhap.split()]
                while len(list_moi) != 3:
                    chuoi_nhap = input("Type all scores in one line, each separated by a space: ")
                    list_moi = [float(x) for x in chuoi_nhap.split()]
                while smaller_equal_10 == False:
                    if any(x > 10 for x in list_moi):
                        chuoi_nhap = input("Type all scores in one line, each separated by a space: ")
                        list_moi = [float(x) for x in chuoi_nhap.split()]
                    else:
                        smaller_equal_10 = True
                d_hien_tai[:] = list_moi
                print("Edited all scores!")
            except ValueError:
                print("Error: Input value is not a number.")
        else:
            print("Invalid Choice!")

    #return d_thuong_xuyen, d_giua_ky, d_cuoi_ky
