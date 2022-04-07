# step through sudoku array start to finish
# enter numbers starting with 1 
# -> if number < 9 is valid: set back to 0 and move on

# rinse & repeat, decreasing the valid threshold each time
from solver_v1.classes import Iterator
from solver_v1.functions import number_is_valid


def figure_absolutes(sudoku_puzzle: list[int]) -> list[int]:
  """ Fill the fields in a sudoku that can absolutely only be that number, beginning with 9, working down to 1. """

  working_solution = sudoku_puzzle.copy()

  for sweep in range(9, 0, -1):
    for index in range(len(working_solution)):

      # skip locked value
      if working_solution[index] > 0:
        continue

      # start entering values
      for value in range(1, sweep + 1):
        working_solution[index] = value

        # and checking them  -  if it can be more than just the sweep, we'll reset and move on
        if number_is_valid(index, working_solution) and value != sweep:
          working_solution[index] = 0
          break
        elif number_is_valid(index, working_solution) and value == sweep:
          pass

  return working_solution