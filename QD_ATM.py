class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        try:
            deposite_amount = int(input("\nYour currently have "+str(self.balance)+ " $\nHow much money do you want to deposite?\n"))
            self.balance = self.balance + deposite_amount
            print(str(deposite_amount)+"$ have been deposited to your account.\nThe current amount is "+str(self.balance)+"$")
        except:
            print('\nPlease enter a valid number!')

    def withdraw(self):
        try:
            withdraw_amount = int(input("\nYour currently have "+str(self.balance)+ " $\nHow much money do you want to withdraw?\n"))
            if withdraw_amount <= self.balance:
                self.balance = self.balance - withdraw_amount
                print(str(withdraw_amount)+ "$ have been withdrawn from your account.\nThe current amount in your Account is "+str(self.balance)+"$")
            else:
                print("You dont have enough money to perform this withdrawal")
        except:
            print('\nPlease enter a valid number!')
    
    def login(self):
        psw = input(f"Please put in the Account Password: ")
        while( psw != "123456"):
            psw = input("Please put in the CORRECT password: ")            
        else:
            self.start()


    def GetBalance(self):
        print("Your Balance is "+str(self.balance)+"$")

    def start(self):
        while(True):
            action = input("\nEnter -1- to check your Balance\nEnter -2- to Withdraw Money\nEnter -3- to Deposite Money\nEnter -4- to Log Out of your Account\n")
            if(action ==  "1"):
                self.GetBalance()
            elif(action == "2"):
                self.withdraw()
            elif(action == "3"):
                self.deposit()
            elif(action=="4"):
                print("You have been logged out of your Account")
                break
            else:
                print("Please input a valid option")

account = Account("QazimD", 1500)
account.login()