marks = int(input("Enter your marks :"))

if(marks >= 90):
  print("Excellent")
elif(marks < 90 and marks >= 80):
  print("Very Good")
elif(marks < 80 and marks >= 70):
  print("Good")
elif(marks < 70 and marks >= 60):
  print("You can do better")
else:
  print("This is not cup of your tea, do something else")