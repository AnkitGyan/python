for i in range(1,15):
  print(i, end=" ") 

x = input("Enter your first number :")
y = input("Enter your second number :")
temp = x
x = y
y = temp
print(x)
print(y)
