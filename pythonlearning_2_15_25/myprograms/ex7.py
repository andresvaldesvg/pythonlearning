# If Statements

# Example 1: Simple if statement
if 5 < 6:
    # This block will execute because 5 is less than 6
    print("Yes, 5 is less than 6")
    print("Everybody knows that")
    print("I am a genius")

# Example 2: If-else statement
if 10 > 20:
    # This block will not execute because 10 is not greater than 20
    print("This will not be printed")
else:
    # This block will execute because the if condition is false
    print("10 is not greater than 20")

# Example 3: If-elif-else statement
number = 15
if number < 10:
    # This block will not execute because number is not less than 10
    print("Number is less than 10")
elif number == 15:
    # This block will execute because number is equal to 15
    print("Number is 15")
else:
    # This block will not execute because one of the above conditions is true
    print("Number is greater than 10 but not 15")

# Example 4: Nested if statements
age = 18
if age >= 18:
    # This block will execute because age is greater than or equal to 18
    print("You are an adult")
    if age >= 65:
        # This block will not execute because age is not greater than or equal to 65
        print("You are a senior citizen")
    else:
        # This block will execute because the nested if condition is false
        print("You are not a senior citizen")
else:
    # This block will not execute because the outer if condition is true
    print("You are not an adult")



