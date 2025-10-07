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

