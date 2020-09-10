class BankAccount():

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
        self.money = 0

    def deposite(self):
        print(self.owner_name + " You added Rs-/ ",self.balance)

    def Update_balace(self, amount):
        self.balance= self.balance + amount
        print(self.owner_name + " Your total balance is ", self.balance)

    def set_withdraw(self, money):
        self.money = money
        if int(self.money) > int(self.balance):
            print(self.owner_name + " You can't withdraw the money")
        else:
            b = int(self.balance) - int(self.money)
            print("you withdraw the amount of Rs-/", self.money)
            print("Remaining money in your balance is Rs-/",b)

obc = BankAccount("Yaman",12000)
obc.deposite()
obc.Update_balace(8796)
obc.set_withdraw(1234)


romey = BankAccount("Hanna", 63527)
romey.deposite()
romey.Update_balace(5978)
romey.Update_balace(9876)
romey.set_withdraw(3467)


julie = BankAccount("Julie", 987674)
julie.deposite()
julie.set_withdraw(3865829)


leonard = BankAccount("sheldon", 150000000)
leonard.deposite()
leonard.set_withdraw(77969697)
