import random
<<<<<<< HEAD
from procrastination_helper.data.excusesData import custom_excuse_templates
=======
from procrastination_helper.data import excusesData
>>>>>>> origin

def get_custom_excuse(task):
    """Returns a personalized excuse based on the task using random templates."""
    template = random.choice(excusesData.custom_excuse_templates)
    return template.format(task=task)
