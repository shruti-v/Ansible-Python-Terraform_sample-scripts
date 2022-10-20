ask_user = input("enter username = ")
ask_pass = input("enter password = ")

credentials = ['username' , 'password']

creds = {}

creds = creds.fromkeys(credentials)

creds['username'] = ask_user
creds['password'] = ask_pass


if ask_user == 'admin' and ask_pass == 'admin':
    print("Authentication successful")
    print(creds)
    
elif (ask_user == 'admin' and ask_pass != 'admin'):
        print("Incorrect password")
        
elif (ask_user != 'admin' and ask_pass != 'admin'):
    print("Incorrect Username & Password")

else:
    print("Incorrect Username")
