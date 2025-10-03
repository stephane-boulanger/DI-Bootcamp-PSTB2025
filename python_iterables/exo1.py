# 🌟 Exercise 1 : Lists
# Instructions
# Write Python code to complete the following tasks.

# Given a list [1, 2, 3, 4], print out all the values in the list one by one.

number_list = [1, 2, 3, 4]
print(number_list)

# Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.

number_list = [1, 2, 3, 4]
for i in number_list:
    print(i * 20)

# Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].

name_list = ["Elie", "Tim", "Matt"]
for i in name_list:
    print(i[0])

# Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6]

number_list = [1, 2, 3, 4, 5, 6]
even_numbers = [i for i in number_list if i % 2 == 0]
print(even_numbers)

# Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].
number_list1 = [1, 2, 3, 4]
number_list2 = [3, 4, 5, 6]
common = list(set(number_list1) & set(number_list2))
print(common)

# Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].

# Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].

# For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].

# Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].

# Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

# Generate a list with the following structure:

# [
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]
