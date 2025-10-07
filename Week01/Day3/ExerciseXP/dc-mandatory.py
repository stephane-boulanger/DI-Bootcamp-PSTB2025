# Exercise 1: Cats
# Key Python Topics:

# Classes and objects
# Object instantiation
# Attributes
# Functions


# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.



# Step 1: Create Cat Objects

# Use the Cat class to create three cat objects with different names and ages.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Chira", 2)
cat2 = Cat("Isis", 8)
cat3 = Cat("Mimi", 14)
# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    elif cat3.age > cat1.age and cat3.age > cat2.age:
        return cat3

# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

print() 

# 🌟 Exercise 2 : Dogs
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)


# Instructions:

# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.



# Step 1: Create the Dog Class

# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “ goes woof!”.
# Create a jump() method that prints “ jumps cm high!”, where x is height * 2.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Step 2: Create Dog Objects

# Create davids_dog and sarahs_dog objects with their respective names and heights.

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Kelly", 20)

# Step 3: Print Dog Details and Call Methods

# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

print(f"David's dog: {davids_dog.name} is {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print()  

# Affichage des détails de Sarah's dog
print(f"Sarah's dog: {sarahs_dog.name} is {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

print()
# Step 4: Compare Dog Sizes

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same size")
