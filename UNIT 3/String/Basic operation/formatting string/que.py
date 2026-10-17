st1 = 'Mango'
for i in range(len(st1)):
  print(st1[i])

st = 'NH-24, Delhi Hapur By Vijay Nagar 201009'
alphabet = 0
digit = 0
for val in st:
  if val.isalpha():
    alphabet = alphabet +1
    if val.isdigit():
      digit = digit +1
print(f"Total No of alphabet")
