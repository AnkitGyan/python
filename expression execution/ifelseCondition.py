food = input("food :")

Eat = "Yes" if food == "Cake" or "cake" else "No"
print(Eat)

age = int(input("Enter age for vote :"))

vote = ("Go to School", "Choose your government") [age >= 18]
print(vote)

salary = int(input("Enter salary :"))

nirmala = salary*(0.05, 0.18) [salary > 1200000]
print(nirmala)