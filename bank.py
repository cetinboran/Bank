import json

class Bank():

    def __init__(self, Name) -> None:
        self.name = Name
    
    def Authentication(self, customerList=list):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in customerList:
            if user.username == username.lower() and user.password == password.lower():
                return user
            else:
                continue