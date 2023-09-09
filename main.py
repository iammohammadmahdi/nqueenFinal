from queenSolver import Solver_Queen
import os
#####################################################

os.system('cls')
n = int(input('Enter n: '))
chess=Solver_Queen(n)
chess.solve_queen()