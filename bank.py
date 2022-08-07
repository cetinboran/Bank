import json

class Bank():
    def Authentication(self, customerList=list):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in customerList:
            if user.username == username.lower() and user.password == password.lower():
                return user
            else:
                continue