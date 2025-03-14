class shape:
  def area(self):
    pass
class rectangle(shape):
  def __init__(self,l,b):
    self.l=l
    self.b=b  
  def area(self):
    return self.l*self.b
class circle(shape):
  def __init__(self,r):
    self.r=r
  def area(self):
    return 3.14*self.r*self.r
shapes=[rectangle(4,5),circle(3)]
for shape in shapes:
  print("Area :",shape.area())