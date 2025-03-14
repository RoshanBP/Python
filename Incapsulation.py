#incapsulation
class sushma:
  def __init__(self):
    self.pub="ok"
    self.__rajesh="not ok"
  def thirisha_private(self):
    print(self.__rajesh)
neha=sushma()
print(neha.pub)
neha.thirisha_private()