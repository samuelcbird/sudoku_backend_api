from solver_v1.functions import number_is_valid


def solve_sudoku_puzzle(sudoku_puzzle: list[int]) -> list[int]:
  ORIGINAL_INPUT: list[int] = sudoku_puzzle

  solution_iteration_index: int = 0
  # previous_iteration_index: int = None # use this in case we're backtracking and land upon a locked value
  working_solution: list[int] = sudoku_puzzle

  while solution_iteration_index < 80:
    # check for locked value
    if ORIGINAL_INPUT[solution_iteration_index] > 0:
      solution_iteration_index += 1
      continue

    while working_solution[solution_iteration_index] > 10:

      # if IndexError:
      #   print(f'index {solution_iteration_index}')
      #   print(f'solution length {len(solution_iteration_index)}')
      #   print(f'value {working_solution[solution_iteration_index]}')

      working_solution[solution_iteration_index] += 1

      if working_solution[solution_iteration_index] > 9:
        working_solution[solution_iteration_index] = 0
        solution_iteration_index -= 1
        break
      elif number_is_valid(solution_iteration_index, working_solution):
        solution_iteration_index += 1
        break

  return working_solution
