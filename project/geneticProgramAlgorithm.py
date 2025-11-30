import random
from treeStructure import Node


def combine_story(a, b):
    return a + " " + b


def generate_story():
    return random.choice(SIMPLE_TEXT)

FUNCTION_SET = {
    "COMBINE": {
        "level": 2,
        "func": combine_story
    }
}

SIMPLE_TEXT = [
    "the hero wakes",
    "the forest is silent",
    "a shadow emerges",
    "the journey begins",
]

print(generate_story())