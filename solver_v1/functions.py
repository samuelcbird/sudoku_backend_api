def create_square_slice(index: int, whole_puzzle: list[int]) -> list[int]:
  block_to_slice: list[int] = []
  slice_to_return: list[int] = []

  sudoku_blocks: list[list[int]] = [
    [0,  1,  2,  9,  10, 11, 18, 19, 20],
    [3,  4,  5,  12, 13, 14, 21, 22, 23],
    [6,  7,  8,  15, 16, 17, 24, 25, 26],
    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],
    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]
  ]

  for block in sudoku_blocks:
    if block.count(index) > 0:
      block_to_slice = block
      break

  for index in block_to_slice:
    slice_to_return.append(whole_puzzle[index])

  return slice_to_return


def create_vertical_slice(index: int, whole_puzzle: list[int]) -> list[int]:
  top_line_index: int = index % 9
  slice_to_return: list[int] = []

  for i in range(top_line_index, 80, 9):
    slice_to_return.append(whole_puzzle[i])

  return slice_to_return
  

def create_horizontal_slice(index: int, whole_puzzle: list[int]) -> list[int]:
  start_of_row: int = index

  while start_of_row % 9 != 0:
    start_of_row -= 1

  return whole_puzzle[start_of_row:start_of_row+9]


def number_is_valid(index: int, whole_puzzle: list[int]) -> bool:
  index_value = whole_puzzle[index]

  if create_square_slice(index, whole_puzzle).count(index_value) > 1:
    return False
  elif create_vertical_slice(index, whole_puzzle).count(index_value) > 1:
    return False
  elif create_horizontal_slice(index, whole_puzzle).count(index_value) > 1:
    return False

  return True
  