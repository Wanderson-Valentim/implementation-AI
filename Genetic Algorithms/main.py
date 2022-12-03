from genetic_algorithms import run_the_algorithm

num_of_iterations = 10
max_it = 100
size_population = 150
mutation_rate = 0.2

print(f'Foram encontrados {run_the_algorithm(num_of_iterations, max_it, size_population, mutation_rate)} resultados com população {size_population}')