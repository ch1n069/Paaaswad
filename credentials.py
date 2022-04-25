import random 
import string

# this will be used to help generate a custom password for


class Credentials():

    user_credentials = []


    def __init__(self,platform,user_account_username,account_password):
        '''created instaces of the  credentials'''


        self.platform = platform
        self.user_account_username = user_account_username
        self.account_password = account_password

    def save_credentials(self):
        '''defining method to save our credentials'''


        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        '''method to delete saved credential'''

        Credentials.user_credentials.remove(self)



    @classmethod
    def find_by_platform(cls,platform):
        '''finds account using platform'''

        for credentials in cls.user_credentials:
            if credentials.platform == platform:
                return credentials
        return False

    
    @classmethod
    def display_credentials(cls):
        '''display all the saved accounts'''


        return cls.user_credentials

    @classmethod
    def generate_password(cls,password_length):
        '''function generates a random password'''


        characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
        #characters from where the password will come from

        #getlength of required password
        gen = string.ascii_letters + string.digits + string.digits
        password = ''.join(random.choice(gen) for i in range(password_length))

        return password 
    
