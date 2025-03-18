import random
from .data.excusesData import custom_excuse_templates

def get_custom_excuse(task):
    """Returns a personalized excuse based on the task using random templates."""
    template = random.choice(custom_excuse_templates)
    return template.format(task=task)
