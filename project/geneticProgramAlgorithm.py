import random
from treeStructure import Node


def combine_story(a, b):
    return a + " " + b

def generate_endnode():
    return random.choice(SIMPLE_TEXT)

def evaluate_tree(node):
    if node.is_terminal():
        return node.value
    
    function_name = FUNCTION_SET[node.value]
    function_info = function_name["function"]
    
    for child in node.children:
        child_values = evaluate_tree(child)
    return function_info(*child_values)

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
        "function": combine_story
    }
}

SIMPLE_TEXT = [
    "the hero wakes",
    "the forest is silent",
    "a shadow emerges",
    "the journey begins",
]


tree = generate_random_tree(max_depth=3)

def check_structure(node):
    if not isinstance(node.children, list):
        print("ERROR: children is not a list:", node, "->", node.children)
    else:
        for child in node.children:
            check_structure(child)

check_structure(tree)
print("Check complete.")