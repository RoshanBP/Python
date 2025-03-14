class bank:
  def__init__(self,balance=0):
  self.balance=balance
  def deposit(self,amount):
    self.balance+=amount
    print(f"current balance is {self.balance}")
  def withdraw(self,amount):
    if amount>self.balance:
      print("insufficient balance")
    else:
      self.balance-=amount
      print(f"current balance is {self.balance}")