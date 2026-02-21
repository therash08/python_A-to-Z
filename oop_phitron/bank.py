class bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print (f'fokira. you can withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print (f'bank fokir hoye jabe.you cant not more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print (f'here is your money {amount}')
            print(f'your balance after withdraw{self.balance}')
        
dbbl = bank(15000)
dbbl.withdraw(2500)
dbbl.withdraw(250000000)
dbbl.withdraw(1000)

brac = bank(4000)
brac.deposit(20000)
brac.deposit(2000)
print(brac.get_balance())