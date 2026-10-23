class student:
    College_name = "ABESEC"
    def __init__(self):
        pass
    
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    getAverage = lambda self: sum(self.marks)/len(self.marks)

s1 = student("Ankit", 20, [98, 97, 99])
s2 = student("Rohit", 21, [90, 85, 88])

print(s1.name + " " + str(s1.age) + " " + student.College_name)
print(s2.name + " " + str(s2.age) + " " + student.College_name)
print("Average marks of " + s1.name + ": " + str(s1.getAverage()))
print("Average marks of " + s2.name + ": " + str(s2.getAverage()))