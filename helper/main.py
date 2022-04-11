from solver_v2.main import solver_v2


def helper(input: list[int]) -> list[int]:
  solution: list[int] = solver_v2(input.copy())

  incorrect_indexes: list[int] = []

  for i in range(81):
    if input[i] != solution[i] and input[i] != 0:
      incorrect_indexes.append(i)

  return incorrect_indexes
