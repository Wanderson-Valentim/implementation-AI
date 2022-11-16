import random

class Board:
  def __init__(self, dimension = 8) -> None:
    self.board = [[0 for x in range(dimension)] for i in range(dimension)]
    self.dimension = dimension
    
  def fill_board(self, positions):
    for column in range(self.dimension):
      row = positions[column]
      self.board[row][column] = 1
      
  def print_board(self):
    for index in range(self.dimension):
      print(self.board[index])
  
  def number_of_attacks(self, positions):
    number_of_attacks = 0
    
    for column in range(self.dimension):
      if(column < (self.dimension - 1)):
        row = positions[column]
        
        number_of_attacks += self.__traverse_row(column, row)
        number_of_attacks += self.__traverse_diagonally_ascending(column, row)
        number_of_attacks += self.__traverse_diagonally_descending(column, row)
      
    return number_of_attacks
  
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
      

def generate_positions(board_dimension):
  positions = []
  #positions = [4,5,6,3,4,5,6,5]
  
  for i in range(board_dimension):
    row = random.randint(0, (board_dimension - 1))
    positions.append(row)
    
  return positions


def main():
  dimension = 8
  board = Board(dimension)
  positions = generate_positions(dimension)

  print(positions)
  board.fill_board(positions)
  board.print_board()
  print(board.number_of_attacks(positions))

main()