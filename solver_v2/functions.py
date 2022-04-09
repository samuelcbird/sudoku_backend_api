# step through sudoku array start to finish
# enter numbers starting with 1 
# -> if number < 9 is valid: set back to 0 and move on

# rinse & repeat, decreasing the valid threshold each time
from solver_v1.classes import Iterator
from solver_v1.functions import number_is_valid


def figure_absolutes(sudoku_puzzle: list[int]) -> list[int]:
  """ Fill the fields in a sudoku that can absolutely only be that number, beginning with 9, working down to 1. """

  working_solution: list[int] = sudoku_puzzle.copy()
  changes_in_last_sweep: bool = True

  while changes_in_last_sweep:
    changes_in_last_sweep = False
    for index in range(len(working_solution)):

      # skip the locked value / value we've entered
      if working_solution[index] > 0:
        continue
    
      valid_values: list[int] = []
      # start checking values
      for value in range (1, 10):
        working_solution[index] = value

        if number_is_valid(index, working_solution):
          valid_values.append(value)
      
      # if there's only one valid value we'll keep it, otherwise reset to 0
      if len(valid_values) == 1:
        working_solution[index] = valid_values[0]
        changes_in_last_sweep = True
      else:
        working_solution[index] = 0


  return working_solution