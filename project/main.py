from markovAlgorithm import MarkovChain
from geneticProgramAlgorithm import (
    generate_random_tree,
    evaluate_tree,
    setup_markov_model,
    initialize_population,
    fitness_function,
    mortal_kombat,
    select_parents,
    crossover,
    mutate,
)

def main():
    #arbitrary text to educate the Markov model
    text = """
    Once upon a time in a land far, far away, there lived a young princess who dreamed of adventure.
    Every day, she would gaze out of her castle window, longing to explore the world beyond the walls.
    One day, a mysterious traveler arrived at the castle gates, bringing tales of distant lands and hidden treasures.
    The princess knew that this was her chance to embark on the journey she had always dreamed of.
    With a heart full of courage and excitement, she bid farewell to her family and set off on an adventure that would change her life forever.
    """
    
    ##markov model setup
    markov = MarkovChain()
    markov.educate(text)
    setup_markov_model(markov)

    #construct a random population
    population = initialize_population(6, 3)

    print("Generated Stories from Population:")
    for i, t in enumerate(population):
        print(f"\nTree {i + 1}:")
        print(t)
        print("Evaluated Story:", evaluate_tree(t))
    
    print ("\nFitness Scores:")
    for i, t in enumerate(population):
        score = fitness_function(t)
        print(f"Tree {i + 1} Fitness: {score}")

    print("\nMortal Kombat Tournament:")
    winner = mortal_kombat(population, fitness_function)
    print("Winner Tree:", winner)
    print("Winner Story:", evaluate_tree(winner))
    print("\nWinner Fitness Score:", fitness_function(winner))

    print("\nSelecting Parents for Crossover:")
    parent1, parent2 = select_parents(population, fitness_function)
    print("Parent 1 Tree:", parent1)
    print("Parent 1 Story:", evaluate_tree(parent1))
    print("Parent 1 Fitness Score:", fitness_function(parent1))
    print("Parent 2 Tree:", parent2)
    print("Parent 2 Story:", evaluate_tree(parent2))
    print("Parent 2 Fitness Score:", fitness_function(parent2))

    print("\nCrossover Result:")
    child1, child2 = crossover(parent1, parent2)
    print("Child 1 Tree:", child1)
    print("Child 1 Story:", evaluate_tree(child1))
    print("Child 1 Fitness Score:", fitness_function(child1))
    print("\nChild 2 Tree:", child2)
    print("Child 2 Story:", evaluate_tree(child2))
    print("Child 2 Fitness Score:", fitness_function(child2))

    print("\nMutation Result - Child 1:")
    mutated_child = mutate(child1, max_depth=3)
    print("Mutated Child Tree:", mutated_child)
    print("Mutated Child Story:", evaluate_tree(mutated_child))
    print("Mutated Child Fitness Score:", fitness_function(mutated_child))


if __name__ == "__main__":
    main()
