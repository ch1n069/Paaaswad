class Users:

    user_list = []

    '''created instance of the class'''

    def __init__(self,firstname,username,password):
        self.firstname = firstname
        self.username = username
        self.password = password

    def save_user(self):
        '''save user to list '''

        Users.user_list.append(self)

    def delete_user(self):
        '''delete user '''

        Users.user_list.remove(self)

    


    
