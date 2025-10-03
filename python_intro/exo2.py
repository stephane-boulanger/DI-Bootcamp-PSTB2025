# Instructions
# Write a program that will calculate cat’s and dog’s years based on human years:

# I have a cat and a dog. I got them at the same time as kitten/puppy. That was humanYears years ago. Print their respective ages now as [humanYears,catYears,dogYears]

# NOTES:

# humanYears >= 1 humanYears are whole numbers only

# Cat Years 15 cat years for first year +9 cat years for second year +4 cat years for each year after that

# Dog Years 15 dog years for first year +9 dog years for second year +5 dog years for each year after that

# example of output:

# human_years = 10
# #output: [10, 56, 64]

# human_years = 1
# #output: [1, 15, 15]

# human_years = 2
# #output [2, 24, 24]


# test the program with the following values:

# human_years = 10
# human_years = 1
# human_years = 2

def cat_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    else:
        cat = 24 + (human_years - 2) * 4
        dog = 24 + (human_years - 2) * 5
        return [human_years, cat, dog]

for y in (10, 1, 2):
    print(cat_dog_years(y))
