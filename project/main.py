from markovAlgorithm import MarkovChain
from geneticProgramAlgorithm import (
    evaluate_tree,
    setup_markov_model,
    fitness_function,
    print_tree,
    run_evolution,
    compute_self_bleu_population,
    initialize_population,
    compute_self_bleu_individual,

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

    population = initialize_population(5, 3)
    stories = [evaluate_tree(t) for t in population]
    self_bleu_scores = compute_self_bleu_individual(stories)

    print("=== Initial Stories ===")
    for index, s in enumerate(stories):
        print("\nStory ", index, ":", s)

    print("\n=== Stories ===")
    for i, s in enumerate(self_bleu_scores):
        print(f"Story {i+1}: {s}")

  

if __name__ == "__main__":
    main()
