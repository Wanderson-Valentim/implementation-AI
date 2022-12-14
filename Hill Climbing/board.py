import random

class Board:
  def __init__(self, dimension = 8, positions = []) -> None:
    self.board = [[0 for x in range(dimension)] for i in range(dimension)]
    self.board_states = [[0 for x in range(dimension)] for i in range(dimension)]
    self.dimension = dimension
    self.__positions = positions
    self.number_of_attacks = 0
    
  def get_positions(self):
    return self.__positions
  
  def set_positions(self, positions):
    self.__positions = positions
    self.board = [[0 for x in range(self.dimension)] for i in range(self.dimension)]
    self.fill_board()
    self.__generate_state()
    self.set_number_of_attacks()
  
  def generate_positions(self):
    positions = []
    for i in range(self.dimension):
      row = random.randint(0, (self.dimension - 1))
      positions.append(row)
    
    self.set_positions(positions)
    
  def print_board(self):
    for index in range(self.dimension):
      print(self.board[index])
  
  def print_board_states(self):
    for index in range(self.dimension):
      print(self.board_states[index])
  
  def fill_board(self):
    for column in range(self.dimension):
      row = self.__positions[column]
      self.board[row][column] = 1
  
  #Função responsável por obter o número de rainhas que se atacam. 
  #Analisa por coluna em ordem crescente as peças que se atacam com a peça da presente na coluna.
  #A contagem é feita analisando a linha e as diagonais da peça.
  def set_number_of_attacks(self):
    number_of_attacks = 0
    
    for column in range(self.dimension):
      if(column < (self.dimension - 1)):
        row = self.__positions[column]
        
        number_of_attacks += self.__traverse_row(column, row)
        number_of_attacks += self.__traverse_diagonally_ascending(column, row)
        number_of_attacks += self.__traverse_diagonally_descending(column, row)
      
    self.number_of_attacks = number_of_attacks

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

  #Essa função é a responsável por gerar o tabuleiro de estados, onde possui os valores que serão utilizados pela função objetivo.
  def __generate_state(self):
    for i in range(self.dimension):
      for j in range(self.dimension):
        copy_positions = self.__positions.copy()
        copy_positions[i] = j
        aux_board = Board(self.dimension, copy_positions)
        aux_board.fill_board()
        aux_board.set_number_of_attacks()
        self.board_states[j][i] = aux_board.number_of_attacks