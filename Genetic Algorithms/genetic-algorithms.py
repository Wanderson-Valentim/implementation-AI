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
    boards[i].proportion = round((boards[i].number_of_no_attacks*100)/total_fitness_values)
  
  #print(boards)
  boards.sort(key=lambda board: board.proportion, reverse=True)
  #print(boards)
  
  return boards

def crossover(index, dimension, parent1, parent2):
  divider = random.randint(2, (len(parent1) - 2))
  
  positions1 = parent1[slice(0,divider)] + parent2[slice(divider, len(parent2))]
  positions2 = parent2[slice(0,divider)] + parent1[slice(divider, len(parent2))]
  
  child1 = Board(index, dimension, positions1)
  child2 = Board(index, dimension, positions2)
  
  return [child1, child2]

def genetic_algorithm():
  max_it = 100
  dimension = 8
  size_population = 150
  
  population = generate_population(size_population)
  geration = 0
  
  while geration < max_it:
    new_population = []
    for i in range(size_population):
      parent1 = population[0].positions
      parent2 = population[1].positions
      childs = crossover(i, dimension, parent1, parent2)
      #FALTA PARTE DE MUTAR
      new_population += childs

    population += new_population
    population = get_proportions(population)[slice(size_population)]

    geration += 1
  
  print(population[0].number_of_no_attacks)

genetic_algorithm()
