# Ask the user for their favorite food
favorite_food = input("What is your favorite food? ")

# Check if the favorite food is "Rice Pudding"
if favorite_food.lower() == "rice pudding":
    # If the input is "Rice Pudding", print a positive response
    print("Yes so nice!")
else:
    # If the input is not "Rice Pudding", print a negative response
    print("Yuck!")

# Print a thank you message regardless of the input
print("Thanks for playing.")
