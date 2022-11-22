import math
import random
from board import Board

def generate_population(size):
  boards = []
  
  for i in range(size):
    board = Board(i+1)
    boards.append(board)
    
  return get_proportions(boards)

def get_total_fitness_values(boards):
  total_fitness_values = 0 
  
  for i in range(len(boards)):
    total_fitness_values += boards[i].number_of_no_attacks
    
  return total_fitness_values

#Função destinada a escolher indivíduos de forma diretamente proporcional à sua função de adaptação.
#Além disso ordena o array contendo a população pelo valor da proporção em ordem descrescente.
def get_proportions(boards):
  total_fitness_values =  get_total_fitness_values(boards)
  
  for i in range(len(boards)):
    boards[i].proportion = (boards[i].number_of_no_attacks*100)/total_fitness_values
  
  boards.sort(key=lambda board: board.proportion, reverse=True)
  
  return boards

def select_parents(population):
  generate_rate = (math.floor(random.random() * 10) / 10) * 100
  size_population = len(population)
  proportions = 0
  parents = []
  
  for i in range(size_population):
    proportions += population[i].proportion

    if generate_rate <= proportions:
      parents.append(population[i])
      
      if i == (size_population - 1):
        parents.append(population[i-1])
      else:
        parents.append(population[i+1])
      
      break
  
  return parents

def crossover(index, dimension, parent1, parent2):
  divider = random.randint(2, (len(parent1) - 2))
  
  positions1 = parent1[slice(0,divider)] + parent2[slice(divider, len(parent2))]
  positions2 = parent2[slice(0,divider)] + parent1[slice(divider, len(parent2))]
  
  child1 = Board(index, dimension, positions1)
  child2 = Board(index, dimension, positions2)
  
  return [child1, child2]

def mutate(childs, mutation_rate, dimension):
  for i in range(len(childs)):
    generate_rate = math.floor(random.random() * 10) / 10
    
    if generate_rate == mutation_rate:
      column = random.randint(0, dimension - 1)
      row = random.randint(0, dimension - 1)
      positions = childs[i].get_positions()
      positions[column] = row
      childs[i].set_positions(positions)
    
  return childs

def genetic_algorithm(max_it, size_population, mutation_rate):
  population = generate_population(size_population)
  new_population = []
  dimension = 8
  geration = 0
  
  while geration < max_it:
    for i in range(size_population):
      parents = select_parents(population)
      childs = crossover(i, dimension, parents[0].get_positions(), parents[1].get_positions())
      childs = mutate(childs, mutation_rate, dimension)
      new_population += childs

    population += new_population
      
    population = get_proportions(population)
    
    population = population[slice(size_population)]
    
    population = get_proportions(population)
    
    if population[0].number_of_no_attacks == 28:
      #print(f'Iteração {geration + 1}, Posições: {population[0].get_positions()}, Fitness: {population[0].number_of_no_attacks}, Proporção: {population[0].proportion}')
      #population[0].print_board()
      geration += 1
      break
    
    #print(f'Iteração {geration + 1}, Posições: {population[0].get_positions()}, Fitness: {population[0].number_of_no_attacks}, Proporção: {population[0].proportion}')

    geration += 1
  
  return [geration, population[0]]

def run_the_algorithm(num_of_iterations, max_it, size_population, mutation_rate):
  number_of_ideal_solutions = 0
  
  for i in range(num_of_iterations):
    solution = genetic_algorithm(max_it, size_population, mutation_rate)
    if solution[1].number_of_no_attacks == 28: number_of_ideal_solutions += 1
    print(f'Iteração {solution[0]}, Posições: {solution[1].get_positions()}, Fitness: {solution[1].number_of_no_attacks}, Proporção: {solution[1].proportion}')
  
  return number_of_ideal_solutions

print(f'Foram encontrados {run_the_algorithm(10, 100, 100, 0.2)} resultados com população 100')
print()
print(f'Foram encontrados {run_the_algorithm(10, 100, 150, 0.2)} resultados com população 150')
print()
print(f'Foram encontrados {run_the_algorithm(10, 100, 200, 0.2)} resultados com população 200')