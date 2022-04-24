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

    return Users.user_exist(username)

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

    print("
          _____                    _____                    _____                    _____                _____                    _____                    _____                    _____     _____          
         /\    \                  /\    \                  /\    \                  /\    \              /\    \                  /\    \                  /\    \                  /\    \   /\    \         
        /::\    \                /::\    \                /::\    \                /::\    \            /::\____\                /::\    \                /::\____\                /::\____\ /::\    \        
       /::::\    \              /::::\    \              /::::\    \              /::::\    \          /:::/    /               /::::\    \              /:::/    /               /:::/    / \:::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \        /:::/    /               /::::::\    \            /:::/    /               /:::/    /   \:::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \      /:::/    /               /:::/\:::\    \          /:::/    /               /:::/    /     \:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    /:::/____/               /:::/__\:::\    \        /:::/    /               /:::/    /       \:::\    \    
   /::::\   \:::\    \      /::::\   \:::\    \       \:::\   \:::\    \       \:::\   \:::\    \   |::|    |               /::::\   \:::\    \      /:::/    /               /:::/    /        /::::\    \   
  /::::::\   \:::\    \    /::::::\   \:::\    \    ___\:::\   \:::\    \    ___\:::\   \:::\    \  |::|    |     _____    /::::::\   \:::\    \    /:::/    /      _____    /:::/    /        /::::::\    \  
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \  /\   \:::\   \:::\    \ |::|    |    /\    \  /:::/\:::\   \:::\    \  /:::/____/      /\    \  /:::/    /        /:::/\:::\    \ 
/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/::\   \:::\   \:::\____\/::\   \:::\   \:::\____\|::|    |   /::\____\/:::/  \:::\   \:::\____\|:::|    /      /::\____\/:::/____/        /:::/  \:::\____\
\::/    \:::\  /:::|____|\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /|::|    |  /:::/    /\::/    \:::\  /:::/    /|:::|____\     /:::/    /\:::\    \       /:::/    \::/    /
 \/_____/\:::\/:::/    /  \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/ |::|    | /:::/    /  \/____/ \:::\/:::/    /  \:::\    \   /:::/    /  \:::\    \     /:::/    / \/____/ 
          \::::::/    /            \::::::/    /    \:::\   \:::\    \       \:::\   \:::\    \     |::|____|/:::/    /            \::::::/    /    \:::\    \ /:::/    /    \:::\    \   /:::/    /          
           \::::/    /              \::::/    /      \:::\   \:::\____\       \:::\   \:::\____\    |:::::::::::/    /              \::::/    /      \:::\    /:::/    /      \:::\    \ /:::/    /           
            \::/____/               /:::/    /        \:::\  /:::/    /        \:::\  /:::/    /    \::::::::::/____/               /:::/    /        \:::\__/:::/    /        \:::\    \\::/    /            
             ~~                    /:::/    /          \:::\/:::/    /          \:::\/:::/    /      ~~~~~~~~~~                    /:::/    /          \::::::::/    /          \:::\    \\/____/             
                                  /:::/    /            \::::::/    /            \::::::/    /                                    /:::/    /            \::::::/    /            \:::\    \                   
                                 /:::/    /              \::::/    /              \::::/    /                                    /:::/    /              \::::/    /              \:::\____\                  
                                 \::/    /                \::/    /                \::/    /                                     \::/    /                \::/____/                \::/    /                  
                                  \/____/                  \/____/                  \/____/                                       \/____/                  ~~                       \/____/                   
                                                                                                                                                                                                              
")










