"""
This module provides a function to retrieve random motivational quotes about procrastination.
Source of quotes: https://www.goodreads.com/quotes/tag/procrastination
"""

import random
from procrastinationhelper.data.quotesData import quotes


def get(num_quotes=1):
    """
    Returns random motivational quotes about procrastination. Accepts number of quotes to return, or defaults to 1 if no argument.
    """
    num_quotes = min(num_quotes, len(quotes))
    
    if num_quotes < len(quotes):
        ret_quotes = random.sample(quotes, num_quotes)
    else:
        ret_quotes = quotes.copy()
        random.shuffle(ret_quotes)
    
    formatted_quotes = [f"{q['text']} - {q['author']}" for q in ret_quotes]
    
    if num_quotes == 1:
        return formatted_quotes[0]
    else:
        return "\n".join(formatted_quotes)
    