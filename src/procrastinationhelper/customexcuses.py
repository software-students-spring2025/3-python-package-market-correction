import random


def get_custom_excuse(task):
    """Returns a personalized excuse based on the task using random templates."""
    template = random.choice(custom_excuse_templates)
    return template.format(task=task)



custom_excuse_templates = [
    "I can't do {task} right now because I need to finish my snack.",
    "I'm too busy to {task} at the moment; my cat needs attention.",
    "I would love to {task}, but I have to binge-watch my favorite show first.",
    "I can't {task} right now; I'm waiting for the pizza delivery.",
    "I need to take a break from {task} to recharge my brain.",
    "I can't focus on {task} because I'm too busy daydreaming.",
]

sample_tasks = [
    "homework",
    
]

