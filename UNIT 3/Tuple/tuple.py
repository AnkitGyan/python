a = 1
condition1 = 1
while condition1 < 5:
  condition2 = 1
  while condition2 <= condition1:
    print(a, end=" ")
    a = a + 1
    condition2 = condition2  + 1
  condition1 = condition1 + 1
  print()