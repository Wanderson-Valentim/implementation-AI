import math
from board import Board

def main():
  no_results = 0
  repetitions = 10
  amount = 0
  dimension = 8
  game = Board(dimension)
  
  for x in range(repetitions):
    count = 0
    while True:
      count += 1
      game.generate_positions()
      
      minimum = 28
      
      while True:
        for i in range(dimension):
          for j in range(dimension):
            if minimum > game.board_states[j][i]:
              minimum = game.board_states[j][i]
              position = (j,i)

        if minimum == game.number_of_attacks:
          break
        else:
          positions = game.get_positions().copy()
          positions[position[1]] = position[0]
          game.set_positions(positions)
      
      if game.number_of_attacks == 0:
        #print(f"Houve resultados na {count}ª iteração\n")
        #print(f"Posições: {game.get_positions()}\n")
        #print(f"Tabuleiro:")
        #game.print_board()
        break
      else: 
        #print(f"Núero de ataques: {game.number_of_attacks}\n")
        #print(f"Posições: {game.get_positions()}\n")
        #print(f"Tabuleiro:")
        #game.print_board()
        no_results += 1
        
    amount += count
      
  print(f"Média de iterações: {math.ceil(amount/repetitions)}")
  print(f"Número de iterações sem resultados: {no_results}")

main()

