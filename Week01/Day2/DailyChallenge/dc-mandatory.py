# Daily Challenge: Dictionaries
# Last Updated: October 7th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# In this challenge, you will enhance your understanding of Python dictionaries, string manipulation, and working with list data structures. You’ll practice iterating over strings, updating dictionaries, and handling data types, all fundamental skills in programming.



# 🛠️ What you will create
# You will create a Python script that processes user input to map the positions of each letter in a given word into a dictionary. This will involve string indexing, dictionary manipulation, and ensuring data types are appropriately handled.



# Challenge
# Ask a user for a word.
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list, and those lists are values.

# Examples
# “dodo” ➞ { “d”: [0, 2], “o”: [1, 3] }
# “froggy” ➞ { “f”: [0], “r”: [1], “o”: [2], “g”: [3, 4], “y”: [5] }
# “grapes” ➞ { “g”: [0], “r”: [1], “a”: [2], “p”: [3], “e”: [4], “s”: [5] }

# 1) Demander un mot à l'utilisateur
word = input("Enter a word: ")

# 2) Créer un dictionnaire vide
positions = {}

# 3) Parcourir chaque lettre avec son index
for index, letter in enumerate(word):
    # 4) Si la lettre n'est pas encore une clé, on la crée
    if letter not in positions:
        positions[letter] = [index]
    # 5) Sinon, on ajoute simplement le nouvel index à la liste existante
    else:
        positions[letter].append(index)

# 6) Afficher le résultat
print(positions)
