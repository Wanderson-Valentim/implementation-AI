import math
from board import Board

def hill_climbing(repetitions):
  amount = 0
  dimension = 8
  game = Board(dimension)
  
  for rep in range(repetitions):
    count = 0
    while True:
      count += 1
      game.generate_positions()
      
      minimum = math.inf
      
      while True:
        for i in range(dimension):
          for j in range(dimension):
            #Função objetivo que pega o menor valor dentre a quantidades de pares de rainhas que se atacam
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
        print(f"-------- {rep+1}ª GERAÇÃO --------")
        print(f"Houve resultados na {count}ª iteração")
        print(f"Posições: {game.get_positions()}")
        print(f"Tabuleiro:")
        game.print_board()
        print()
        break
        
    amount += count
      
  print("-------- RESULTADO FINAL --------")
  print(f"Média com {repetitions} iterações: {math.ceil(amount/repetitions)}")
