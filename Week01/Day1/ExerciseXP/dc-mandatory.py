# Exercise mandatory

# Exercise

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# * Basic Python syntax and operations.
# * How to interact with the user through input and output.
# * Working with different data types including lists, tuples, and sets.
# * Conditional statements and loops in Python.

# 🛠️ What you will create
# * Various small programs that demonstrate fundamental programming concepts such as loops, conditions, and data structures.

# 🌟 Exercise 1 : Hello World
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

hello = "Hello World "
print(hello*4)

# 🌟 Exercise 2 : Some Math
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

power = 99**3

calcul = power*8

print(calcul)

# 🌟 Exercise 3 : What’s your name ?
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

my_name = "Stephane"
ask_name = input("What's your name?")

if my_name == ask_name:
    print(f"Great {ask_name}, are you my clone? ")
else:
    print("Sorry")
    
# 🌟 Exercise 4 : Tall enough to ride a roller coaster
# 1. Write code that will ask the user for their height in centimeters.
# 2. If they are over 145cm print a message that states they are tall enough to ride.
# 3. If they are not tall enough print a message that says they need to grow some more to ride.

# 🌟 Exercise 5 : Favorite Numbers
# Key Python Topics:
# * Sets
# * Adding/removing items in a set
# * Set concatenation (using union)

# Instructions:
# * Create a set called my_fav_numbers and populate it with your favorite numbers.
# * Add two new numbers to the set.
# * Remove the last number you added to the set.
# * Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# * Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#    * Note: Sets are unordered collections, so ensure no duplicate numbers are added.

# 🌟 Exercise 6: Tuple
# Key Python Topics:
# * Tuples (immutability)

# Instructions:
# * Given a tuple of integers, try to add more integers to the tuple.
# * Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

# 🌟 Exercise 7: List Manipulation
# Key Python Topics:
# * Lists
# * List methods: append, remove, insert, count, clear

# Instructions:
# * You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# * Remove "Banana" from the list.
# * Remove "Blueberries" from the list.
# * Add "Kiwi" to the end of the list.
# * Add "Apples" to the beginning of the list.
# * Count how many times "Apples" appear in the list.
# * Empty the list.
# * Print the final state of the list.

# 🌟 Exercise 8 : Sandwich Orders
# Using the list below :
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"].
# 1. The deli has run out of pastrami, use a while loop to remove all occurrences of Pastrami sandwich from sandwich_orders.
# 2. We need to prepare the orders of the clients:
# 3. Create an empty list called finished_sandwiches.
# 4. One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# 5. After all the sandwiches have been made, print a message listing each sandwich that was made, such as:

# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich