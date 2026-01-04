auth_status = 'auth_status.txt'
accounts = 'acc.csv'

#weak encrypt
def encrypt(s:str):
    h = 0
    for i in s:
        h=h*128+ord(i)
    h = str(h)
    r = ['5', '4', '6', '9', '1', '3', '2', '7', '0', '8']
    h1 = ''
    for i in range(0, len(h)):
        h1 += r[ord(h[i])-48]
    return h1

def check_auth():
    global auth_status
    with open(auth_status, 'r') as file:
        if file.read()=='false':
            return False
        else:
            return True

def register(username, password):
    global accounts
    username = encrypt(username)
    password = encrypt(password)
    with open(accounts, 'a') as file:
        file.write(username+' '+password)

def log_in(username, password):
    global accounts, auth_status
    username = encrypt(username)
    password = encrypt(password)
    logged_in = False
    with open(accounts, 'r') as file:
        for line in file:
            cur_acc = line.split()
            if (cur_acc[0]==username and cur_acc[1]==password):
                with open(auth_status, 'w') as file:
                    logged_in = True
                    file.write(username)
    if logged_in:
        return True
    else:
        return False        

def log_out():
    global auth_status
    with open(auth_status, 'w') as file:
        file.write('')

def change_pass(new_pass):
    global accounts, auth_status
    username = ''
    with open(auth_status, 'r') as file:
        username = file.readline()
    new_pass = encrypt(new_pass)
    lines = []
    with open(accounts, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        cur_acc = lines[i].split()
        if username == cur_acc[0]:
            cur_acc[1] = new_pass
            break
    lines[i] = cur_acc[0]+' '+cur_acc[1]
    with open(accounts, 'w') as file:
        file.writelines(lines)