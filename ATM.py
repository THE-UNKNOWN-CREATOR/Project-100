class Atm(object):
    def __init__(self, atmCard, password):
        self.balance = 20000
        self.atmCard = atmCard
        self.password = password
        start(self)

    def CheckBalance(self):
        print(f"Your current balance is {self.balance}")
        start(self)
        
    def Withdrawal(self):
        a = input("Input Card Number: ")

        if a == self.atmCard:
            p = input("Input password: ")
            if p == self.password:
                am = int(input("Input amount to Withdraw: "))
                self.balance -= am
                self.CheckBalance()
                start(self)
            else :
                print("Invalid password")
                start(self)
        else:
            print("Invalid Card number")
            start(self)

    def Deposit(self):
        a = input("Input Card Number: ")

        if a == self.atmCard:
            p = input("Input password: ")
            if p == self.password:
                am = int(input("Input amount to Deposit: "))
                self.balance += am
                self.CheckBalance()
                start(self)
            else :
                print("Invalid password")
                start(self)
        else:
            print("Invalid Card number")
            start(self)


def start(atm):
    print("Choose an Action: ")
    print("Check Balance - 1")
    print("Withdraw - 2")
    print("Deposit - 3")
    print("Exit - Q")
    i = input("Enter action:  ")

    if i == "1":
        atm.CheckBalance()
    elif i == "3":
        atm.Deposit()
    elif i == "2":
        atm.Withdrawal()
    elif i == "Q":
        return
    else:
        print("invalid input")
        start(atm)


an = input("Input card number(Any number): ")
pp = input("Input your password(Any password): ")
atm = Atm(an, pp)
#start(atm)
