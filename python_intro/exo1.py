# Exercise 1 : Boolean Logic
# Instructions
# enComplete the exercises below by writing an expression in Python to answer the question:

# Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"
print(first)

# Write a comment that says "This is a comment."
comment = "This is a comment"
print(comment)

# Log a message to the terminal that says "I AM A COMPUTER!"
message = "I am a computer!"
print(message)

# Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1 < 2 & 2 < 4:
  print("Math is fun")

# Assign a variable called nope to an absence of value.
nope = None
print(nope)

# Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.

# Calculate the length of the string "What's my length?"
length = "What's my length?"
print(len(length))

length = "What's my length?"
compteur = 0
for caractere in length:
  compteur +=1
print(compteur)


# Convert the string "i am shouting" to uppercase.
shouting = "I am shouting"
print(shouting.upper())

# Convert the string "1000"to the number 1000.
numb_str = "1000"
print(int(numb_str))

# Combine the number 4 with the string "real" to produce "4real".
four = "4"
real = "real"
print(four+real)

# Record the output of the expression 3 * "cool".
cool = "cool "
print(cool*3)

# Record the output of the expression 1 / 0.
expr = "1 / 0"
print(expr)

# Determine the type of [].
brack = type([]) 
print(brack)

# Ask the user for their name, and store it in a variable called name.
user_name =input("Whats your name? ")
print(user_name)
name = user_name
print(name)

# Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" 
# If the number is positive, show a message that says "That number is greater than 0!" 
# Otherwise, show a message that says "You picked 0!.
ask_numb = input("Give me a number ")
print(ask_numb)
numb = int(ask_numb)
if numb < 0:
    print("That number is less than 0!That number is less than 0")
elif numb > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# Find the index of "l" in "apple".
apple = "apple"
print(apple[3])

# Check whether "y" is in "xylophone".
xylo = "xylophone"
res_y = "y" in xylo
print(res_y)

# Check whether a string called my_string is all in lowercase.

my_string = "string"

if my_string == my_string.lower():
    print(True)
else:
   print(False)
