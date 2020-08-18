# Implemented a quiz using if/else structures and variables for scoring

score = 0

answer = input("What does CPU stand for?")
if answer == "central processing unit":
  print("Correct!")
  score += 1  
else:
  print("Sorry, wrong answer.")
  
answer = input("How many bits are in a byte?")
if answer == "8":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")
  
answer = input("Which is bigger: a kilobyte or a megabyte?")
if answer == "megabyte":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")

print ("You scored {} points!".format(score))