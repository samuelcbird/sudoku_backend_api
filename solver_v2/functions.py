# step through sudoku array start to finish
# enter numbers starting with 1 
# -> if number < 9 is valid: set back to 0 and move on

# rinse & repeat, decreasing the valid threshold each time
from solver_v1.classes import Iterator
from solver_v1.functions import number_is_valid


def figure_absolutes(sudoku_puzzle: list[int]) -> list[int]:
  iterator = Iterator()
  working_solution = sudoku_puzzle.copy()

  for sweep in range(9, 0, -1):
    while iterator.getCurrentIteration() < 81:

      if sudoku_puzzle[iterator.getCurrentIteration()] > 0:
        # skip locked value and move on
        iterator.incrementOne()
        continue

      for value in range(1, sweep):
        working_solution[iterator.getCurrentIteration()] = value
        
        if number_is_valid(iterator.getCurrentIteration(), working_solution) and working_solution[iterator.getCurrentIteration()] < sweep:
          working_solution[iterator.getCurrentIteration()] = 0
          iterator.incrementOne()
          break

        iterator.incrementOne()
  
  return working_solution