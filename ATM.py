class Atm(object):
    def __innit__(self, atmCard, password):
        self.balance = 20000
        self.atmCard = atmCard
        self.password = password
        
    def Withdrawal(self):
        a = input("Input Card Number: ")

        if a == self.atmCard:
            p = input("Input password: ")
            if p == self.password:
                am = input("Input amount to Withdraw: ")
                self.balance -= am
            else :
                print("Invalid password")
        else:
            print("Invalid Card number")

    def Deposit(self):
        a = input("Input Card Number: ")

        if a == self.atmCard:
            p = input("Input password: ")
            if p == self.password:
                am = input("Input amount to Deposit: ")
                self.balance += am
            else :
                print("Invalid password")
        else:
            print("Invalid Card number")

    def CheckBalance(self):
        print(self.balance)

def start(atm):
    print("Choose an Action: ")
    print("Check Balance - 1")
    print("Withdraw - 2")
    print("Deposit - 3")
    i = input("Enter action:  ")

    if i == 1:
        atm.CheckBalance()
    elif i == 2:
        atm.Deposit()
    elif i == 3:
        atm.Withdrawal()
    else:
        print("invalid input")
        start(atm)


an = input("Input card number(Any number): ")
pp = input("Input your password(Any password): ")
atm = Atm()
start(atm)
