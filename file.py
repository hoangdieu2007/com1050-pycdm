import csv

fields = ['id', 'name', 'score']
database = 'database.csv'
auth_status = 'auth_status.txt'
accounts = 'acc.csv'

#only using csv

def nuke():
    global database, fields, accounts
    with open(database, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
    with open(accounts, 'w') as file:
        file.write('')

def write_data_csv(id, name, score):
    global database, fields
    with open(database, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writerow({'id':id, 'name':name, 'score':score})

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
        print("Score: ", row['score'])

def showall_csv():
    global database, fields
    with open(database, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print('ID: ',row['id'],", Name: ", row['name'], ", Score: ", row['score'], sep="")

#dictionary processing

datadict = {}

def load_dict():
    global database, datadict
    with open(database, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datadict[row['id']] = {'name' : row['name'], 'score' : row['score']}

def save_dict():
    global database, fields, datadict
    with open(database, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for id in datadict:
            writer.writerow({'id':id, 'name': datadict[id]['name'], 'score' : datadict[id]['score']})

def write_data(id, name, score):
    global datadict
    datadict[id] = {'name' : name, 'score' : score}

def search(id):
    global datadict
    print('Name:', datadict[id]['name'])
    print('Score:', datadict[id]['score'])

def showall():
    global datadict
    for id in datadict:
        print('ID: ', id, ', Name: ', datadict[id]['name'], ', Score: ', datadict[id]['score'], sep='')