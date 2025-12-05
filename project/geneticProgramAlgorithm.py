import random
from markovAlgorithm import MarkovChain
from treeStructure import Node

MARKOV_MODEL = None
SIMPLE_TEXT = []

##Markov model to GP integration
def setup_markov_model(model: MarkovChain):
    global MARKOV_MODEL
    MARKOV_MODEL = model


##GP finction set for tree representation
def combine_story(a, b):
    return a + " " + b

def generate_endnode():
    if MARKOV_MODEL is not None:
        return MARKOV_MODEL.generate_sentence(max_length=8)
    else:
        global SIMPLE_TEXT
        return random.choice(SIMPLE_TEXT)

def evaluate_tree(node):
    if node.is_terminal():
        return node.value
    
    function_info = FUNCTION_SET[node.value]["function"]
    
    child_values = [evaluate_tree(child) for child in node.children]

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
        child = generate_random_tree(depth, current_depth + 1)
        children.append(child)
    
    return Node(func_name, children)


FUNCTION_SET = {
    "COMBINE": {
        "level": 2,
        "function": combine_story
    }
}

##GP population creation functiono
def initialize_population(population_size, tree_depth):
    population = []
    for _ in range(population_size):
        tree = generate_random_tree(tree_depth)
        population.append(tree)
    return population

##Create fitness function
def fitness_function(tree):
    story = evaluate_tree(tree)
    word_count = len(story.split())
    return word_count

def fitness_key(pair):
    return pair[1]

##Create the MORTAL KOMBAT!!! TANDANDANDANDDDAAAAAN
def mortal_kombat(population, fitness_function, torunament_size=3):
    figheters = random.sample(population, torunament_size)
    fatality_scores = [(fighter, fitness_function(fighter)) for fighter in figheters]
    winner = max(fatality_scores, key=fitness_key)[0]    ##select only the fitness score for comparison
    return winner

##Select Parents for Future Crossover
def select_parents(population, fitness_function, tournament_size=3):
    parent1 = mortal_kombat(population, fitness_function, tournament_size)
    parent2 = mortal_kombat(population, fitness_function, tournament_size)
    while parent2 == parent1:
        parent2 = mortal_kombat(population, fitness_function, tournament_size)
    return parent1, parent2

##Crossover functions 
def collect_all_nodes(node, parent=None, index_in_parent=None, result=None):
    if result is None:
        result = []
    result.append((node, parent, index_in_parent))

    if hasattr(node, 'children') and isinstance(node.children, list):
        for index, child in enumerate(node.children):
            collect_all_nodes(child, node, index, result)
    return result

def pick_random_subtree(tree):
    all_nodes = collect_all_nodes(tree)
    selected_node, parent, index_in_parent = random.choice(all_nodes)
    return selected_node, parent, index_in_parent

def crossover(parent1, parent2):
    copied_parent1 = parent1.copy()
    copied_parent2 = parent2.copy()

    subtree1, parent_of_subtree1, index1 = pick_random_subtree(copied_parent1)
    subtree2, parent_of_subtree2, index2 = pick_random_subtree(copied_parent2)

    if parent_of_subtree1 is None:
        new_child1 = subtree2.copy()
    else:
        parent_of_subtree1.children[index1] = subtree2.copy()
        new_child1 = copied_parent1

    if parent_of_subtree2 is None:
        new_child2 = subtree1.copy()
    else:
        parent_of_subtree2.children[index2] = subtree1.copy()
        new_child2 = copied_parent2

    return new_child1, new_child2

##Mutation function
def mutate(tree, max_depth):
    tree_copy = tree.copy()

    node, parent, index = pick_random_subtree(tree_copy)
    mutant_tree = generate_random_tree(depth=max_depth, current_depth=0)

    if parent is None:
        return mutant_tree
    else:
        parent.children[index] = mutant_tree
        return tree_copy