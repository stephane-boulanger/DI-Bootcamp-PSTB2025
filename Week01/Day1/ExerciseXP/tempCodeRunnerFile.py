sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich",
    "Pastrami sandwich"
]

print("Sorry, we're out of pastrami today 🥲")

# Remove all Pastrami sandwiches
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

# Prepare each sandwich (simple for loop)
for sandwich in sandwich_orders:
    print(f"I made your {sandwich.lower()}")
    finished_sandwiches.append(sandwich)