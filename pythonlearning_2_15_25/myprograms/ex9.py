class CarWash:
    def __init__(self, amount):
        # Initialize the CarWash class with the amount of money provided
        self.amount = amount

    def get_wash_type(self):
        # Determine the type of wash based on the amount of money
        if self.amount >= 15:
            return "Premium Wash"
        elif self.amount >= 10:
            return "Standard Wash"
        elif self.amount >= 5:
            return "Basic Wash"
        else:
            return "Insufficient funds for a wash"

def main():
    # Ask the user for the amount of money they have
    amount = float(input("Enter the amount of money you have: "))
    # Create an instance of the CarWash class
    car_wash = CarWash(amount)
    # Get the type of wash based on the amount of money
    wash_type = car_wash.get_wash_type()
    # Print the type of wash
    print(f"Wash type: {wash_type}")

if __name__ == "__main__":
    # Run the main function
    main()
