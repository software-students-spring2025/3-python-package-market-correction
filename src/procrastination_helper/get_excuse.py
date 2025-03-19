import random
from procrastination_helper.data.excusesData import sample_excuses
def get_excuse():
    return random.choice(sample_excuses)
