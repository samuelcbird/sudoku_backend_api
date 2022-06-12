from logic.iterator.iterator import Iterator

class Solution:
  def __init__(self, unsolvedPuzzle: list[int], halfFinishedPuzzle: list[int] = None):
    self.unsolved_puzzle: list[int] = unsolvedPuzzle
    self.half_finished_puzzle: list[int] = halfFinishedPuzzle
    self.finished_puzzle: list[int] = None

  def show_incorrect_answers(self):
    if self.half_finished_puzzle == None:
      # raise error
      return
    else:
      solution: list[int] = self.full_solution(self.unsolved_puzzle)
      half_finished: list[int] = self.half_finished_puzzle
      incorrect_indexes: list[int] = []

      for i in range(81):
        if half_finished[i] != solution[i]:
          if half_finished[i] == 0:
            pass
          else:
            incorrect_indexes.append(i)
              
      return incorrect_indexes

  def full_solution(self, puzzleToSolve: list[int] = None):
    unsolved: list[int]

    if puzzleToSolve is None:
      unsolved = self.unsolved_puzzle.copy()
    else :
      unsolved = puzzleToSolve

    find_absolute_answers: list[int] = self._figure_absolutes(unsolved)
    return self._backtracker(find_absolute_answers)

  def _figure_absolutes(self, sudoku_puzzle: list[int]) -> list[int]:
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

          if self._number_is_valid(index, working_solution):
            valid_values.append(value)
        
        # if there's only one valid value we'll keep it, otherwise reset to 0
        if len(valid_values) == 1:
          working_solution[index] = valid_values[0]
          changes_in_last_sweep = True
        else:
          working_solution[index] = 0


    return working_solution


  def _backtracker(self, sudoku_puzzle: list[int]) -> list[int]:
    iterator = Iterator()
    working_solution: list[int] = sudoku_puzzle.copy()

    while iterator.getCurrentIteration() < 81:
      # check for locked value
      if sudoku_puzzle[iterator.getCurrentIteration()] > 0:

        # if we reversed and we're on locked value, reverse again
        if iterator.getPreviousIteration() > iterator.getCurrentIteration():
          iterator.decrementOne()
          continue

        # otherwise skip locked value and move on
        iterator.incrementOne()
        continue

    
      # try a number at the current index, starting at 1
      while working_solution[iterator.getCurrentIteration()] < 10:
        working_solution[iterator.getCurrentIteration()] += 1

        # if we've tried 1 - 9 and none are valid, we'll go back
        if working_solution[iterator.getCurrentIteration()] > 9:
          working_solution[iterator.getCurrentIteration()] = 0
          iterator.decrementOne()
          break

        # if if a number is valid we'll move on 
        elif self._number_is_valid(iterator.getCurrentIteration(), working_solution):
          iterator.incrementOne()
          break

    return working_solution


  def _create_square_slice(self, index: int, whole_puzzle: list[int]) -> list[int]:
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


  def _create_vertical_slice(self, index: int, whole_puzzle: list[int]) -> list[int]:
    top_line_index: int = index % 9
    slice_to_return: list[int] = []

    for i in range(top_line_index, 80, 9):
      slice_to_return.append(whole_puzzle[i])

    return slice_to_return
    

  def _create_horizontal_slice(self, index: int, whole_puzzle: list[int]) -> list[int]:
    start_of_row: int = index

    while start_of_row % 9 != 0:
      start_of_row -= 1

    return whole_puzzle[start_of_row:start_of_row+9]


  def _number_is_valid(self, index: int, whole_puzzle: list[int]) -> bool:
    index_value = whole_puzzle[index]

    if self._create_square_slice(index, whole_puzzle).count(index_value) > 1:
      return False
    elif self._create_vertical_slice(index, whole_puzzle).count(index_value) > 1:
      return False
    elif self._create_horizontal_slice(index, whole_puzzle).count(index_value) > 1:
      return False

    return True