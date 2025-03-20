"""
Example program demonstrating all functions in the procrastination_helper package.
"""

from procrastination_helper import quotes
from procrastination_helper.get_excuse import get_excuse
from procrastination_helper.customexcuses import get_custom_excuse
from procrastination_helper.list_of_excuses import get_excuse_list
from procrastination_helper.delay_timer import delay_timer
import random
import time

def demonstrate_quotes():
    print("\n===== DEMONSTRATING QUOTES MODULE =====")
    
    # Get a single quote
    print("\n1. Getting a single quote:")
    single_quote = quotes.get(num_quotes=1)
    print(single_quote)
    
    # Get multiple quotes
    print("\n2. Getting multiple quotes:")
    multiple_quotes = quotes.get(num_quotes=3)
    print(multiple_quotes)

def demonstrate_random_excuse():
    print("\n===== DEMONSTRATING RANDOM EXCUSE MODULE =====")
    
    print("\nGetting a random excuse:")
    excuse = get_excuse()
    print(f"I couldn't finish my work because {excuse}")

def demonstrate_custom_excuse():
    print("\n===== DEMONSTRATING CUSTOM EXCUSES MODULE =====")
    
    tasks = ["finishing my homework", "attending the meeting", "responding to emails"]
    print("\nGetting custom excuses for different tasks:")
    for task in tasks:
        custom_excuse = get_custom_excuse(task)
        print(f"Excuse for {task}: {custom_excuse}")

def demonstrate_excuse_list():
    print("\n===== DEMONSTRATING EXCUSE LIST MODULE =====")
    
    print("\nGetting a list of 3 random excuses:")
    excuses = get_excuse_list(3)
    for i, excuse in enumerate(excuses, 1):
        print(f"Excuse {i}: {excuse}")

def demonstrate_delay_timer():
    print("\n===== DEMONSTRATING DELAY TIMER =====")
    print("This function helps you procrastinate for a set time with humorous excuses")
    
    print("\nNormally, this function would run interactively for several minutes.")
    print("For this demo, we'll show a simplified version with a 3-second timer.")
    
    # Import the actual function but modify it for the demo
    print("\nSimulated output of delay_timer(1) but using seconds instead of minutes:")
    
    # Simulate the delay_timer with a much shorter delay
    print("Procrastinating for 3 seconds...")
    time.sleep(3)
    
    excuses = [
        "That went by fast! You deserve 5 more minutes.",
        "You can't stop now! You're in the middle of something (probably).",
        "Studies show that short breaks boost productivity... take another one!"
    ]
    print(random.choice(excuses))
    
    print("\nIn the full function, you would be prompted:")
    print("Do you want to extend? (yes/no): ")
    print("And based on your answer, you'd get more time or be told to get back to work.")
    
    print("\nTo use the actual function:")
    print("from procrastination_helper.delaytimer import delay_timer")
    print("delay_timer(5)  # Procrastinate for 5 minutes")

def main():
    print("==================================================")
    print("PROCRASTINATION HELPER PACKAGE DEMONSTRATION")
    print("==================================================")
    print("This example demonstrates all functions in the package.")
    
    demonstrate_quotes()
    demonstrate_random_excuse()
    demonstrate_custom_excuse()
    demonstrate_excuse_list()
    demonstrate_delay_timer()
    
    print("\n==================================================")
    print("END OF DEMONSTRATION")
    print("Thanks for exploring the Procrastination Helper package!")
    print("==================================================")

if __name__ == "__main__":
    main()