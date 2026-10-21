def sum(n):
  if(n == 1 or n == 0): return n

  return n + sum(n-1)

print(sum(5))