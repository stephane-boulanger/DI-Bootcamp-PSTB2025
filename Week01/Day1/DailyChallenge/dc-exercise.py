# <!-- Daily Challenge : String and Lists
# Last Updated: October 7th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# How to manipulate lists in Python to generate sequences based on input criteria.
# Techniques for string manipulation to modify and format strings based on specific rules.
# Developing logic to handle and remove consecutive duplicate characters from strings.


# 🛠️ What you will create
# A Python program that takes a number and generates a list of its multiples up to a specified length.
# A Python script that processes user input to remove consecutive duplicate characters from strings, enhancing your understanding of string handling.


# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples



# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102] -->

number = int(input("What's your number?"))

length = int(input("What's the lenght?"))

# Generate the list of multiples
multiples = [number * i for i in range(1, length + 1)]
  
  
print("Here are your multiples:", multiples)



# <!-- Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

# Examples



# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon" --> 

# 1) Demander une chaîne à l'utilisateur
