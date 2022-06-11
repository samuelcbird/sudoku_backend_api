from solver_v2.functions import figure_absolutes
from solver_v1.main import backtracker

def solver_v2(sudoku_puzzle: list[int]) -> list[int]: 
  half_solved = figure_absolutes(sudoku_puzzle)
  return backtracker(half_solved)
