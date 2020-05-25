d={1001:{'Name':'Sachin','Bal':10000,'Pwd':'redhat@123'},
   1002:{'Name':'Samyak','Bal':20000,'Pwd':'redhat'},
   1003:{'Name':'Rajat','Bal':30000,'Pwd':'1234'}}

last_account=1003
from getpass import getpass
def main_menu():
    s='''1.Signup\n2.Login\n3.Exit'''
    print(s)
    ch=int(input('Enter Choice between 1 to 3:  '))
    if ch==1:
        signup()
    elif ch==2:
        login()
    else:
        exit()
def exit():
    print('\n')
    print('Thanks for using our service...........)')
    print('...............Exiciting................')
def signup():
    print('\n')
    print('Now you are at signup page')
    global d,last_account
    reg={'Name':input('Enter your Name'),'Bal':int(input('Enter Balance')),'Pwd':getpass('Enter Password')}
    last_account+=1
    d[last_account]=reg
    print('Account Created Successfully')
    print('Now you can login')
    print('Your Account Number is: ',last_account)
    main_menu()
def login():
    print('\n')
    print('Now you are at login page')
    acc=int(input('Enter Account Number'))
    if acc in d:
        pwd=getpass('Enter Password')
        if pwd==d[acc]['Pwd']:
            print('Login Successfully')
            print(f"Hello {d[acc]['Name']}")
            main_menu()
        else:
            print('Invalid Password')
            login()
    else:
        print('Account not exist')
        print('Please do signup before login')          
        main_menu()
