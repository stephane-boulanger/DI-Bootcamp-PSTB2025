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

# 🌟 Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Lists


# Instructions:

# Create a Song class with a method to print song lyrics line by line.



# Step 1: Create the Song Class

# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


# Example:

# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]
print()

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
          print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

print()

# 🌟 Exercise 4 : Afternoon at the Zoo
# Goal:

# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.


# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        
# 2. Implement the __init__() method:

# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.

# 3. Add a method add_animal(new_animal):

# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.

 
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"✅ {new_animal} added to {self.zoo_name}")
        else:
            print(f"⚠️  {new_animal} is already in the zoo")

    # 4. Add a method get_animals():
      # This method prints all animals currently in the zoo. 
    def get_animals(self):
            print(f"Animals currently in {self.zoo_name}:")
            for animal in self.animals:
                print(f"- {animal}")


    # 5. Add a method sell_animal(animal_sold):
    # This method checks if a specified animal exists on the animals list and if so, remove from it.

    def sell_animal(self, animal_sold):
            if animal_sold in self.animals:
                self.animals.remove(animal_sold)
                print(f"{animal_sold} has been sold and removed from the zoo.")
            else:
                print(f"{animal_sold} is not found in the zoo.")
    # 6. Add a method sort_animals():

    # This method sorts the animals alphabetically.
    # It also groups them by the first letter of their name.
    # The result should be a dictionary where:
    # Each key is a letter.
    # Each value is a list of animals that start with that letter.

    def sort_animals(self):
            #self.animals.sort()
            # Sort the animal list alphabetically
            self.animals.sort()
            grouped = {}

        
            # Group animals by first letter
            for animal in self.animals:
                first_letter = animal[0].upper()
                if first_letter not in grouped:
                    grouped[first_letter] = [animal]
                else:
                    grouped[first_letter].append(animal)
            self.groups = grouped
            return grouped

    # 7. Add a method get_groups():



    def get_groups(self):
        if not hasattr(self, 'groups'):  # ← Vérifie d'abord si l'attribut existe
            print("\nNo groups found. Please run sort_animals() first.")
        else:
            print(f"\nAnimal groups in {self.zoo_name}:")
            for letter, names in self.groups.items():
                print(f"{letter}: {names}")



# Create the zoo
my_zoo = Zoo("Safari Park")

# Add animals
my_zoo.add_animal("Elephant")
my_zoo.add_animal("Zebra")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Eagle")
my_zoo.add_animal("Lemur")
my_zoo.add_animal("Tiger")

# Display all animals
my_zoo.get_animals()

# Sort and group them
my_zoo.sort_animals()

# Display grouped animals
my_zoo.get_groups()


