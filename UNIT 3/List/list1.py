nes = [[1,2,3],[4,5,6],[5,6,7]]
for i in range(len(nes)):
  for j in range(len(nes[0])):
    print(nes[i][j],end=' ')
  print()

nestedlist = [[1,2],[3,4],[5,6,7]]
newlist=[]
for i in range(len(nestedlist)):
  for j in range(len(nestedlist[i])):
    newlist.append(nestedlist[i],[j])
    print(newlist)