import random
from treeStructure import Node


def combine_story(a, b):
    return a + " " + b

def generate_endnode():
    return random.choice(SIMPLE_TEXT)

def generate_random_tree(depth):
    if depth == 0:
        return Node(random.choice(SIMPLE_TEXT))
    
    func_name = random.choice(list(FUNCTION_SET.keys()))
    func_info = FUNCTION_SET[func_name]
    children = [generate_random_tree(depth - 1) for _ in range(func_info["level"])]
    return Node(func_name, children)


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

print(generate_endnode())