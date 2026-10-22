f = open("C:\\Users\\ankit\\OneDrive\\Desktop\\Python\\fileHandling\\demo.txt", "r")

data = f.read()
print(data)
print(type(f))
print(type(data))
f.close()