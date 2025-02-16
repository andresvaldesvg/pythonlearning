#!/usr/bin/env python3
"""
Simple Hello World Program with Enhanced Visual Elements
This program demonstrates basic Python concepts with a visually appealing interface.
Author: Your Name
Date: 2024
"""

import time
import sys
from typing import Optional

def print_fancy_header() -> None:
    """Prints a decorative header for the program."""
    print("*" * 50)
    print("*" + " " * 18 + "WELCOME TO PYTHON" + " " * 17 + "*")
    print("*" * 50)

def get_user_name() -> str:
    """
    Prompts the user for their name with input validation.
    
    Returns:
        str: The validated user name
    """
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")

def animate_text(text: str) -> None:
    """
    Displays text with a simple animation effect.
    
    Args:
        text (str): The text to animate
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def main() -> None:
    """Main program function."""
    try:
        # Display welcome header
        print_fancy_header()
        
        # Get user input
        name = get_user_name()
        
        # Create personalized message
        message = f"Hello, {name}! Welcome to the Python world!"
        
        # Display animated message
        animate_text(message)
        
        # Display closing message
        print("\nThank you for using this program!")
        print("*" * 50)
        
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()