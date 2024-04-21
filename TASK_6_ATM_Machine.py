#Create a program that simulates the all atm functionalities and operations (Check balance, Deposit, Withdraw)

#First of all make the class by the name of ATM
class ATM_Machine:
    def __init__(self):
        self.balance = 0
    
    #Function to Deposit the amount
    def Deposit_amount(self):
        amount = int(input("Enter the amount you want to deposit : "))
        self.balance += amount
        print("You have successfully Deposit your amount : ", amount)
    
    #Function to Withdraw the amount
    def Withdraw_amount(self):
        amount = int(input("Enter the amount you want to withdraw : "))
        if self.balance >= amount:
            self.balance -= amount
            print("You have successfully withdraw your amount : ", amount)
        
        else:
            print("Insufficient Balance")
        
    #Function to Check your amount
    def Check_amount(self):
        print("Net Available Balance : ", self.balance)

#Create the objective of the class

atm = ATM_Machine()

atm.Deposit_amount()
atm.Withdraw_amount()
atm.Check_amount()