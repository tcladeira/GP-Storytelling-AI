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
    print_tree,
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


if __name__ == "__main__":
    main()
