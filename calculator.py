class Calculator:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def add(self):
    return self.a+self.b
  def subtract(self):
    return self.a-self.b
  def multiply(self):
    return self.a*self.b
  def divide(self):
    return self.a/self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=Calculator(a,b)
while True:
  print("1.Addition")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")
  print("5.Exit")
  choice=int(input("Enter your choice: "))
  if choice==1:
    print("Result: ",c.add())
  elif choice==2:
    print("Result: ",c.subtract())
  elif choice==3:
    print("Result: ",c.multiply())
  elif choice==4:
    print("Result: ",c.divide())
  elif choice==5:
    break
