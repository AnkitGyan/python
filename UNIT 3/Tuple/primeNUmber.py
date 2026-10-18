N = int(input("Enter a positive number :"))
condition = 2
bool = 1
if N == 1 :
  print("1 is niether prime nor composite")
if N == 2: print("2 is prime number")
while condition < N:
  for i in range (2, condition, 1):
    if(condition % i == 0): bool = 0
    break
  if(bool == 1):
    print(f"{condition} is prime number")
  condition = condition + 1