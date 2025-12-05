from markovAlgorithm import MarkovChain
from geneticProgramAlgorithm import (
    evaluate_tree,
    setup_markov_model,
    fitness_function,
    print_tree,
    run_evolution,

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
    population = run_evolution(
        population_size = 10,
        fitness_function = fitness_function,
        generations = 5,
        max_depth = 4,
    )

    best_tree = max(population, key=fitness_function)
    print("\nBest Evolved Story Tree:")
    print_tree(best_tree)
    best_story = evaluate_tree(best_tree)
    print("\nGenerated Story:")
    print(best_story)


if __name__ == "__main__":
    main()
