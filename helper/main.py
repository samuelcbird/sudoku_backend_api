from solver_v2.main import solver_v2


def helper(unsolved_sudoku: list[int], attempted_sudoku: list[int]) -> list[int]:
  solution: list[int] = solver_v2(unsolved_sudoku)

  incorrect_indexes: list[int] = []

  for i in range(81):
    if attempted_sudoku[i] != solution[i]:
      if attempted_sudoku[i] == 0:
        pass
      else:
        incorrect_indexes.append(i)
        
  return incorrect_indexes
