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
    grammar_check

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

    population = initialize_population(10, 5)
    stories = [evaluate_tree(individual) for individual in population]
    self_bleu_scores = compute_self_bleu_individual(stories)

    print("\n=== SELF-BLEU TEST ===")
    for i, ind in enumerate(population):
        print(f"\n--- Individual {i+1} ---")
        print_tree(ind)
        print("STORY:", stories[i])
        print("WORD COUNT:", len(stories[i].split()))
        print("SELF-BLEU:", self_bleu_scores[i])

        # Evaluate creativity fitness (length minus penalty)
        fitness = fitness_function(ind, stories, self_bleu_scores, index=i)
        print("CREATIVITY FITNESS:", fitness)
        print(f"Story {i+1} Grammar Errors:", grammar_check(stories[i]))

if __name__ == "__main__":
    main()
