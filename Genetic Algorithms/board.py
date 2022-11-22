import random
import datetime

class Board:
  def __init__(self, iteration_number, dimension = 8, positions = []) -> None:
    self.board = [[0 for x in range(dimension)] for i in range(dimension)]
    self.dimension = dimension
    self.__positions = positions
    self.iteration_number = iteration_number
    self.id = f'{iteration_number}-{datetime.datetime.now().time()}'
    self.proportion = 0
    
    if len(positions) != 0:
      self.fill_board()
    else:
      self.generate_positions()
      self.fill_board()
      
    self.number_of_no_attacks = self.get_number_of_no_attacks()
  
  def generate_positions(self):
    positions = []
    for i in range(self.dimension):
      row = random.randint(0, (self.dimension - 1))
      positions.append(row)
    
    self.__positions = positions
    
  def set_positions(self, positions):
    self.__positions = positions
    self.fill_board()
    self.number_of_no_attacks = self.get_number_of_no_attacks()
    
  def get_positions(self):
    return self.__positions
    
  def fill_board(self):
    board = [[0 for x in range(self.dimension)] for i in range(self.dimension)]
    for column in range(self.dimension):
      row = self.__positions[column]
      board[row][column] = 1

    self.board = board
    
  def print_board(self):
    for index in range(self.dimension):
      print(self.board[index])
  
  #Função de adaptação (fitness) (𝑓𝑎) que calcula o nº de pares de rainhas que não se atacam. A solução ótima é dada por 𝑓𝑎 = 28
  #A função busca o total de pares rainhas que se atacam e subtrai da solução ótima para obter o número de pares que não se atacam.
  def get_number_of_no_attacks(self):
    number_of_attacks = 0
    
    for column in range(self.dimension):
      if(column < (self.dimension - 1)):
        row = self.__positions[column]
        
        number_of_attacks += self.__traverse_row(column, row)
        number_of_attacks += self.__traverse_diagonally_ascending(column, row)
        number_of_attacks += self.__traverse_diagonally_descending(column, row)
      
    return 28 - number_of_attacks
  
  def __traverse_diagonally_ascending(self, column, row):
    number_of_attacks = 0
    
    for i in range((column + 1), self.dimension):
      row -= 1
      
      if row < 0:
        break
      elif self.board[row][i]:
        number_of_attacks += 1
      
    return number_of_attacks

  def __traverse_diagonally_descending(self, column, row):
    number_of_attacks = 0
    
    for i in range((column + 1),self.dimension):
      row += 1
      
      if row > (self.dimension - 1):
        break
      elif self.board[row][i]:
        number_of_attacks += 1
      
    return number_of_attacks

  def __traverse_row(self, column, row):
    number_of_attacks = 0
    
    for i in range((column + 1), self.dimension):
      if self.board[row][i]:
        number_of_attacks += 1
    
    return number_of_attacks