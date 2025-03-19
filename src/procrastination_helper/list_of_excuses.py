import random
<<<<<<< HEAD
from procrastination_helper.data.excusesData import sample_excuses
=======
from .data.excusesData import sample_excuses
>>>>>>> origin

#returns n amount of randmon excuses from the sample_excuses
def get_excuse_list(n):
    return random.sample(sample_excuses, min(n, len(sample_excuses)))
