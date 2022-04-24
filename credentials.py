import random 

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
