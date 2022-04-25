#!/usr/bin/env python 3.8

from user import Users

from credentials import Credentials

def create_new_user(firstname,username,password):
    '''user '''

    new_user = Users(firstname,username,password)
    return new_user

def save_user(user):
    '''save user '''

    return user.save_user()

def delete_user(username):
    '''delete user'''

    return Users.delete_user(username)

def check_existing_user(username):
    '''check user exists'''


    return Users.user_exists(username)



def check_user_password(username, password):
    '''check user entered correct username and password'''

    return Users.check_user(username, password)






def create_new_credentials(platform,user_account_username,account_password):
    ''''create credential for platfor, eg facebook'''


    new_credential = Credentials(
        platform,user_account_username,account_password

    )
    return new_credential


def save_credentials(credentials):
    '''save credentials to the database'''

    credentials.save_credentials()



def display_credentials():
    '''function to display credentials'''


    return Credentials.display_credentials()


def delete_credentials(platform):
    '''delete credentials'''

    return Credentials.delete_credentials(platform)




def find_credentials(user_account_username):

    '''find credentials to delete'''

    return Credentials.find_by_platform(user_account_username)


def generate_password(password_length):
    '''generate random password'''


    return Credentials.generate_password(password_length)


def main():

    print("adle")



    while True:
        print("*"*50)
        print("use the follwing shortcode  to continue \n cc- create a new user account \n lg - login to your account\n  da - display your account\n ex -exit" )
        print("*"*30)

        code = input().lower()
        if code  == 'cc':
            print("create New user account")
            print('*#'*40)
            print("Enter your first name......")
            firstname = input()
            print("enter your username......")
            username = input()
            print("Enter your password......")
            password = input()
            save_user(create_new_user(firstname, username, password))

            print("*"*30)
            print(f"Hello {firstname}. account wa created !!!!!!!! login now")

            print("*"*30)
        elif code == 'lg' :
            print("*"*30)
            print("Enter your username..........")
            username = input()
            print("Enter your password..........")

            password = input()
            if check_existing_user(username):
                if check_user_password(username, password):
                    print("\n")
                    print(f"Welcome to the pass vault: {username} ")
                    print("*"*50)
                    while True:
                        print("select the options provided below\n")
                        print("1. create credential\n 2. view saved credentials\n 3. Delete credentials \n 4.Logout")
                        print("#"*40)
                        choice = int(input())
                        if choice == 1:
                            print("Enter account name you want to create: ")
                            platform = input()
                            print("Enter username of the said account: ")
                            user_account_username = input()
                            print("\n")
                           #allow user to generate password
                            print("*"*50)
                            print("Do you want to generate a new password or Enter your own ?\n \n Enter 1 to generate password\n Enter 2 to user your own password")
                            print("#*"*50)
                            print("\n")
                            choice_1 = int(input())
                            if choice_1 == 1:
                                print("what long do you want the password to be ")

                                password_length = int(input())
                                account_password = generate_password(password_length)
                                print(f"your password is {account_password}")
                            elif choice == 2:
                                print("Enter password of the account ")
                                account_password = input()
                            else:
                                print("Thats a wrong response")

                                #save Credentials
                            save_credentials(create_new_credentials(platform,user_account_username,account_password))
                            print(f"Your new credential with account name '{platform}' and password is '{account_password}' has been saved!!!\n ")
                            print('#'*50)
                        elif choice == 2:
                            print("\n")
                            print("Here are all the credentials in the vault")
                            print("*"*50)

                            if display_credentials():
                                for Platform in display_credentials():
                                    print(f"{Platform.platform} Account name, username:{Platform.user_account_username} and the password is : {Platform.account_password}\n")
                                
                            else:
                                print("no accounts were found")
                                print("//"*30)
                        elif choice == 3:
                            print("Enter account you want to delete")
                            platform_to_delete = input()

                            if find_credentials(platform_to_delete):

                                print(f"account name '{platform_to_delete}' has been deleted")
                                print("/n")
                            else:
                                print("*"*50)
                                print(f"Platform  '{platform_to_delete}' do not exist")
                                print('*'*50)
                        elif choice == 4:
                            print("you have logged out")
                            print("*"*50)
                            break
                        else:
                            print("no such account")
            else:
                print("YOu entered wrong credentials")
        elif code == 'ex':
            print("Goodbye.............")
            break
                    



if __name__ == "__main__":
    main()














