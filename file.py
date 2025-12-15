#written by Tran Vu Duc Khang

import csv

fields = ['id', 'name', 'score']
database = 'database.csv'
auth_status = 'auth_status.txt'
accounts = 'acc.csv'

def nuke():
    global database, fields, accounts
    with open(database, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
    with open(accounts, 'w') as file:
        file.write('')

def write_data(id, name, score):
    global database, fields
    with open(database, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writerow({'id':id, 'name':name, 'score':score})

def search(id):
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
        print("Score: ", row['score'])

def showall():
    global database, fields
    with open(database, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print('ID: ',row['id'],", Name: ", row['name'], ", Score: ", row['score'], sep="")