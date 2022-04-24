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


