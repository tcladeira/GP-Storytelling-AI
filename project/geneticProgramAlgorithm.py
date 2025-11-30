import random
from treeStructure import Node


def combine_story(a, b):
    return a + " " + b

FUNCTION_SET = {
    "COMBINE": {
        "level": 2,
        "func": combine_story
    }
}

SIMPLE_TERMINALS = [
    "the hero wakes",
    "the forest is silent",
    "a shadow emerges",
    "the journey begins",
]

def generate_story():
    return random.choice(SIMPLE_TERMINALS)


print(generate_story())