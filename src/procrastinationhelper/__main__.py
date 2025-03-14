"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import argparse
import quotes as quotes
import random
from customexcuses import custom_excuse_templates

def get_custom_excuse(task):
    """Returns a personalized excuse based on the task using random templates."""
    template = random.choice(custom_excuse_templates)
    return template.format(task=task)


def main():
    """
    Get procrastination quotes and print them out.
    """
    parser = argparse.ArgumentParser(description="Get procrastination quotes")
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Number of quotes to display (default: 1)"
    )
    args = parser.parse_args()
    
    result = quotes.get(num_quotes=args.number)
    
    print("\nProcrastination Wisdom:")
    print(result)
    print("\nNote: More features coming soon!")



if __name__ == "__main__":
    main()

    task = input("What task are you procrastinating on? ")
    excuse = get_custom_excuse(task)
    print(excuse)
    
    