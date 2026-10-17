string = input()
stack = []
b = 1
for item in string:
  if item in ('(', '{' ,'['):
    stack.append(item)
  else:
    if len(stack) == 0:
      b = 0 
      break
    else:
      if(item ==')' and stack[-1]=='(') or (item == '}' and stack[-1]=='{') or (item == ']' and stack[-1] == '['):
        stack.pop()
      else:
        b = 0
        break
    