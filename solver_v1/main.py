from solver_v1.functions import number_is_valid
from solver_v1.classes import Iterator


def solve_sudoku_puzzle(sudoku_puzzle: list[int]) -> list[int]:
  iterator = Iterator()
  ORIGINAL_INPUT: list[int] = sudoku_puzzle
  working_solution: list[int] = sudoku_puzzle.copy()

  while iterator.getCurrentIteration() < 81:
    # check for locked value
    if ORIGINAL_INPUT[iterator.getCurrentIteration()] > 0:

      # if we reversed and we're on locked value, reverse again
      if iterator.getPreviousIteration() > iterator.getCurrentIteration():
        iterator.decrementOne()
        continue

      # otherwise skip locked value and move on
      iterator.incrementOne()
      continue

    
    while working_solution[iterator.getCurrentIteration()] < 10:
      working_solution[iterator.getCurrentIteration()] += 1

      if working_solution[iterator.getCurrentIteration()] > 9:
        
        working_solution[iterator.getCurrentIteration()] = 0
        iterator.decrementOne()
        break

      elif number_is_valid(iterator.getCurrentIteration(), working_solution):

        iterator.incrementOne()
        break

  return working_solution
