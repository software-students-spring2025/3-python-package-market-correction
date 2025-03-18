"""
Main entry point for the procrastination_helper package.
This file is run when the package is executed directly from the command line.
"""
import argparse

from procrastination_helper import quotes, get_excuse, get_custom_excuse, get_excuse_list

def get_procrastination_quotes(num_quotes):
    """
    Get procrastination quotes and return them.
    """
    return quotes.get(num_quotes=num_quotes)

def display_procrastination_wisdom(quotes):
    """
    Display procrastination wisdom quotes.
    """
    print("\nProcrastination Wisdom:")
    print(quotes)
    print("\nNote: More features coming soon!")

def display_sample_excuse():
    """
    Display sample excuse.
    """
    print("Sample excuse: ", get_excuse())

def get_task_and_custom_excuse():
    """
    Get the task input from the user and display a custom excuse.
    """
    task = input("What task are you procrastinating on? ")
    excuse = get_custom_excuse(task)
    print(excuse)

def display_random_excuses(number_of_excuses):
    excuses = get_excuse_list(number_of_excuses)
    print("\nHere are some random excuses for procrastination:")
    for excuse in excuses:
        print(f"- {excuse}")

def main():
    """
    Main function to handle command-line arguments and get excuses.
    """
    parser = argparse.ArgumentParser(description="Get procrastination quotes")
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Number of quotes to display (default: 1)"
    )
    args = parser.parse_args()

    procrastination_quotes = get_procrastination_quotes(args.number)
    display_procrastination_wisdom(procrastination_quotes)

    display_sample_excuse()

    get_task_and_custom_excuse()

if __name__ == "__main__":
    main()
