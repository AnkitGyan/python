l = [1, 2, "ankit", "sharma", 4, 5, 6]
print(*l, sep=", ")
l[2] = "guddu"

tup = (1, 2, "guddu", "pandit", 4, 7)
print(*tup)
for el in tup:
  print(el)
else:
  print(type(tup))

def printHello():
  for i in range(0, 6):
    print("Hello World time", i)

def printHello2(i):
  if(i == 0):
    return
  print("Recursive Hello")
  printHello2(i-1)


printHello()
printHello2(5)

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]

def  countCities(cities_list):
  print("Total cities are : ", len(cities_list))
  
countCities(cities)