import random
from treeStructure import Node


def combine_story(a, b):
    return a + " " + b

def generate_endnode():
    return random.choice(SIMPLE_TEXT)

def generate_random_tree(depth, current_depth=0):
    if current_depth >= depth:     #base case: stop recursion at max depth
        value = generate_endnode()
        return Node(value)
    
    if random.random() < 0.25:  #chance of creating end node before reaching max depth
        value = generate_endnode()
        return Node(value)

    func_name = random.choice(list(FUNCTION_SET.keys()))   #if our tree creation did not stop yet (1/4 chance), then we expand it
    level_tree = FUNCTION_SET[func_name]["level"]

    children = []

    for _ in range(level_tree):
        children = generate_random_tree(depth, current_depth + 1)
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