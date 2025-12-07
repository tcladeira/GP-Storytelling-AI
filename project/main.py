from markovAlgorithm import MarkovChain
from geneticProgramAlgorithm import (
    evaluate_tree,
    setup_markov_model,
    fitness_function,
    print_tree,
    run_evolution,
    compute_self_bleu_individual,
    load_book_to_markov,
    extract_real_sentences,
    setup_terminal_sentences

)

def main():

    cleaned_text = load_book_to_markov("booksample.txt")
    real_sentences = extract_real_sentences(cleaned_text)

    setup_terminal_sentences(real_sentences)
    
    ##markov model setup
    markov = MarkovChain()
    markov.educate(cleaned_text)
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
