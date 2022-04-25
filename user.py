class Users():

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



    @classmethod
    #Above is decorator observing into the whole class that
    def find_user(cls,username):
        '''responsible for findind the user their username'''
        for user in cls.user_list:
            if user.username == username:
                return user



    @classmethod

    def user_exists(cls,username):
        '''check if username is in our given user list'''

        for user in cls.user_list:
            if user.username == username:
                return True
        return False


    @classmethod
    def check_user(cls,username, password):
        '''This block is here will check if user is present and the user
        password is also correct'''


        user = cls.find_user(username)
        if user and user.password == password:
            return True
        return False

    


    
