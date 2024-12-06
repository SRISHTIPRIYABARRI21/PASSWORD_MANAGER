from cryptography.fernet import Fernet

master_pwd = input("what is the master password? ")


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

  
write_key()


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "| password:", passw)

                 
def add():
    name = input('Account name : ')
    pwd = input('Password: ')
    
    with open ('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

    
while True: 
    mode = input("would you like to add a new password or view the existing ones (view, add)? press q to quit ").lower()
    if mode == "q":
        break 
      
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
        
