#!/usr/bin/env python3
"""
Programming Best Practices Demo
A simple program to demonstrate basic programming principles and best practices.
"""

def demonstrate_variables():
    """Shows proper variable naming and usage"""
    print("\n=== Variable Naming Examples ===")
    
    # Good variable names - descriptive and clear
    user_name = "John"
    user_age = 25
    is_student = True
    
    print("Good variable names:")
    print(f"user_name: {user_name}")
    print(f"user_age: {user_age}")
    print(f"is_student: {is_student}")
    
    # Bad variable names - DON'T do this
    print("\nBad variable names (avoid these):")
    print("x = 'John'     # Too vague")
    print("a123 = 25      # Meaningless")
    print("thing = True   # Not descriptive")

def demonstrate_comments():
    """Shows proper commenting practices"""
    print("\n=== Comments Examples ===")
    
    # Single line comment explaining the calculation
    total = 100 + 50  # Adding bonus points to base score
    print("Good comment:", "# Adding bonus points to base score")
    
    print("\nBad comments (avoid these):")
    print("# Adding numbers    # Obvious, doesn't add value")
    print("# This code written by John    # Irrelevant information")

def demonstrate_functions():
    """Shows function organization and documentation"""
    print("\n=== Function Best Practices ===")
    
    def calculate_total(price: float, tax_rate: float = 0.1) -> float:
        """
        Calculates total price including tax.
        
        Args:
            price: Base price of the item
            tax_rate: Tax rate as decimal (default 0.1 or 10%)
            
        Returns:
            Total price including tax
        """
        return price * (1 + tax_rate)
    
    # Example usage
    result = calculate_total(100)
    print("Good function example:")
    print("- Clear name (calculate_total)")
    print("- Documented parameters")
    print("- Has default values")
    print("- Returns meaningful result")
    print(f"Example result: ${result}")

def demonstrate_error_handling():
    """Shows basic error handling practices"""
    print("\n=== Error Handling Examples ===")
    
    try:
        # Attempting risky operation
        number = int(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError:
        print("Error: Please enter a valid number")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("This always runs - good for cleanup")

def main():
    """Main program function"""
    print("=== Programming Best Practices Demo ===")
    print("This program shows basic programming principles")
    
    # Call each demonstration function
    demonstrate_variables()
    demonstrate_comments()
    demonstrate_functions()
    demonstrate_error_handling()
    
    print("\n=== Summary of Best Practices ===")
    print("1. Use clear, descriptive variable names")
    print("2. Write meaningful comments")
    print("3. Organize code into functions")
    print("4. Handle errors appropriately")
    print("5. Document your code")

if __name__ == "__main__":
    main()
