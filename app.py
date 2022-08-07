from customer import Customer
from accounts import Account
from bank import Bank

import json
import os

def init_customers(cust):
    with open("Users.json", "r") as f:
        customers = json.load(f)
    for customer in customers:
        cust.append(Customer(customer["username"], customer["password"]))

def init_accounts(accountList):
    with open("Accounts.json", "r") as f:
        accounts = json.load(f)
    for account in accounts:
        accountList.append(Account(account["customerId"], account["balance"], account["accountName"]))

def readCustomerAccounts(customerAccounts):
    for account in customerAccounts:
        print(f"Id: {account.id}, Balance: {account.balance} Accout Name: {account.accountName}")
    
def readAccounts(accounts):
    for account in accounts:
        print(f"Id: {account.id}, Balance: {account.balance}, Accout Name: {account.accountName}")

def SelectCustomerAccount(customerAccounts):
    readCustomerAccounts(customerAccounts)
    print("\n")

    try:
        accountId = input("Choose your account with ID: ")
        for customerAccount in customerAccounts:

            if int(accountId) == customerAccount.id:
                return customerAccount
            else:
                continue
    except:
        input("Please enter a valid ID")
    
def SelectAccount(accounts):
    readAccounts(accounts)
    print("\n")

    try:
        transferId = int(input("Enter your transfer ID: "))
        for account in accounts:

            if int(transferId) == account.id:
                return account
            else:
                continue
    except:
        input("Please enter a valid ID")

def withdraw_money(customerAccounts):

    customerAccount = SelectCustomerAccount(customerAccounts)

    if customerAccount != None:
        try:
            money = int(input("Çekilecek Parayı Giriniz: "))
            if customerAccount.balance >= money:
                customerAccount.balance -= money
                print("Başarıyla Çekildi")
                input(f"Remaining Balance: {customerAccount.balance} ")
            elif customerAccount.balance < money:
                input("Insufficient amount")
        except:
            input("Please enter a valid number")

def deposit_money(customerAccounts):
    customerAccount = SelectCustomerAccount(customerAccounts)

    if customerAccount != None:
        try:
            money = int(input("Enter the money to be deposited: "))
            if(money > 0):
                customerAccount.balance += money
                input(f"Balance: {customerAccount.balance} ")
            else:
                input("Please enter a valid money amount")
        except:
            input("Please enter a number")

def transfer_money(customerAccounts, accounts):
    customerAccount = SelectCustomerAccount(customerAccounts)
    print("-------------------------------------------------")
    if customerAccount != None:
        targetAccount = SelectAccount(accounts)
        print("-------------------------------------------------")
        if targetAccount != None:
            transferMoney = int(input("Enter the amount of money to send: "))

            if customerAccount.balance >= transferMoney:
                customerAccount.balance -= transferMoney
                targetAccount.balance += transferMoney
                input(f"Remaining Balance: {customerAccount.balance}")
            elif customerAccount.balance < transferMoney:
                input("Insufficient amount")


def updateAccountJSON(accounts):
    account_list = []

    for account in accounts:
        account_dict = {"customerId": account.customer_id, "id": account.id, "balance": account.balance, "accountName": account.accountName}
        account_list.append(account_dict)
        with open("Accounts.json", "w") as json_file:
            json.dump(account_list, json_file, indent=4, sort_keys=False)

def updateCustomerJSON(customers):
    customer_list = []

    for customer in customers:
        customer_dict = {"id": customer.id, "username": customer.username, "password": customer.password}
        customer_list.append(customer_dict)
        with open("Users.json", "w") as json_file:
            json.dump(customer_list, json_file, indent=4, sort_keys=False)



def login_bank(bank, customers, accounts, customerAccounts):
    customer = bank.Authentication(customers)
    if customer != None: 
        for account in accounts:
            if customer.id == account.customer_id:
                customerAccounts.append(account)
                return customer
    else: 
        print("Login Failed")

def register_bank(customers, accounts):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    customer_list = []
    account_list = []


    if len(username) > 3 and len(password) > 3:
        cust = Customer(username, password)
        customers.append(cust)

        updateCustomerJSON(customers)
            
        accountName = input("Enter your account name: ")
        acc = Account(cust.id, 0, accountName)
        accounts.append(acc)

        updateAccountJSON(accounts)

    else:
        input("Lütfen 3 karakterden fazla giriniz.")
    
    
 

def Start():
    accounts = []
    customers = []
    BoranBank = Bank()

    init_customers(customers)
    init_accounts(accounts)

    customerAccounts = []

    
    Login = True
    while Login:
        print("1 - Login")
        print("2 - Register")
        print("9 - Quit")
        command = input(">: ")
        if(command == "1"): 
            customer = login_bank(BoranBank, customers, accounts, customerAccounts)
            break
        elif(command == "2"):
            register_bank(customers, accounts)
        elif(command == "9"): 
            customer = None
            Login = False
            return customer
            
            
    while customer != None and Login == True:
        

        os.system("cls")
        print("1 - Show Accounts")
        print("2 - Withdraw Money")
        print("3 - Deposit Money")
        print("4 - Transfer Money")
        print("9 - Quit")
        command = input(">: ")

        if(command == "9"): customer = None
        elif(command == "1"): 
            readCustomerAccounts(customerAccounts) 
            input("-" * 20)
        elif(command == "2"):
            withdraw_money(customerAccounts)
            updateAccountJSON(accounts)
        elif(command == "3"): 
            deposit_money(customerAccounts)
            updateAccountJSON(accounts)
        elif(command == "4"): 
            transfer_money(customerAccounts, accounts)
            updateAccountJSON(accounts)

Start()