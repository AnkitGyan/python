for i in range(1,6):
  for j in range(1,i+1):
    print(i*i,end=" ")
  print()

for i in range(6,1,-1):
  for j in range(1,i+1):
    print(j*j,end=" ")
  print()

  for i in range(1,5):
    for j in range(4,i,-1):
      print(j,end=" ")
    print()