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
    grammar_check,
    load_book_to_markov,

)

def main():
    #arbitrary text to educate the Markov model
    text1 = """
    Once upon a time in a land far, far away, there lived a young princess who dreamed of adventure.
    Every day, she would gaze out of her castle window, longing to explore the world beyond the walls.
    One day, a mysterious traveler arrived at the castle gates, bringing tales of distant lands and hidden treasures.
    The princess knew that this was her chance to embark on the journey she had always dreamed of.
    With a heart full of courage and excitement, she bid farewell to her family and set off on an adventure that would change her life forever.
    """

    text2 = load_book_to_markov("booksample.txt")
    
    ##markov model setup
    markov = MarkovChain()
    markov.educate(text2)
    setup_markov_model(markov)

    final_pop = run_evolution(
        population_size=15,
        max_depth=4,
        generations=5,
        tournament_size=3,
        crossover_rate=0.8,
        mutation_rate=0.2
    )

    best_individual = max(final_pop, key=lambda t: fitness_function(
        t, [evaluate_tree(i) for i in final_pop],
        compute_self_bleu_individual([evaluate_tree(i) for i in final_pop]),
        final_pop.index(t)
    ))

    print("\n=== BEST TREE STRUCTURE ===")
    print_tree(best_individual)
    print("\n=== BEST STORY ===")
    print(evaluate_tree(best_individual))
    print("\n=== BEST FITNESS ===")
    print(fitness_function(
        best_individual,
        [evaluate_tree(i) for i in final_pop],
        compute_self_bleu_individual([evaluate_tree(i) for i in final_pop]),
        final_pop.index(best_individual)
    ))
if __name__ == "__main__":
    main()
