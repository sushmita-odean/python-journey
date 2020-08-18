# Ask user for input and assign it to a variable
name = input("what is your name?")

print(name)

# Combine variables and strings using format()
name = input("What is your name?")
color = input("What is your favourite color?")
food = input("What is your favourite food?") 

print("Well {}, I bet you'd love {} {} then!".format(name, color, food))

# Asking for numbers using int() and adding numbers
siblings = int(input("How many brothers and sisters do you have?"))
total_children = siblings + 1

print("That means your parents have {} children in total.".format(total_children))
