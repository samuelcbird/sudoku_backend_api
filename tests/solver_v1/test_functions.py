import unittest
from solver_v1.functions import create_horizontal_slice, create_square_slice, create_vertical_slice, number_is_valid
from solver_v1.main import solve_sudoku_puzzle

class TestSolverFunctions(unittest.TestCase):

  test_input: list[int] = [
    0, 0, 1, 0, 0, 2, 0, 0, 3,
    0, 0, 4, 0, 0, 5, 0, 0, 6,
    0, 0, 7, 0, 0, 8, 0, 0, 9,
    0, 1, 0, 0, 1, 1, 0, 1, 2,
    0, 1, 3, 0, 1, 4, 0, 1, 5,
    0, 1, 6, 0, 1, 7, 0, 1, 8,
    0, 1, 9, 0, 2, 0, 0, 2, 1,
    0, 2, 2, 0, 2, 3, 0, 2, 4,
    0, 2, 5, 0, 2, 6, 0, 2, 7
  ]

  # expected output for index: 34, whole_puzzle: self.test_input
  expected_square_slice = [0, 1, 2, 0, 1, 5, 0, 1, 8]
  expected_vert_slice = [0, 0, 0, 1, 1, 1, 2, 2, 2]
  expected_horiz_slice = [0, 1, 0, 0, 1, 1, 0, 1, 2]


  def test_create_square_slice(self):
    self.assertEqual(create_square_slice(34, self.test_input), self.expected_square_slice)

  def test_create_horizontal_slice(self):
    self.assertEqual(create_horizontal_slice(34, self.test_input), self.expected_horiz_slice)

  def test_create_vertical_slice(self):
    self.assertEqual(create_vertical_slice(34, self.test_input), self.expected_vert_slice)

  def test_number_is_valid(self):
    self.assertTrue(number_is_valid(68, self.test_input))
    self.assertFalse(number_is_valid(64, self.test_input))

  # -------------------------------------------------------
  # valid sudoku puzzles for testing solve_sudoku_puzzle()
  # -------------------------------------------------------

  puzzle_1 = [
    5, 0, 0, 4, 6, 7, 3, 0, 9,
    9, 0, 3, 8, 1, 0, 4, 2, 7,
    1, 7, 4, 2, 0, 3, 0, 0, 0,
    2, 3, 1, 9, 7, 6, 8, 5, 4,
    8, 5, 7, 1, 2, 4, 0, 9, 0,
    4, 9, 6, 3, 0, 8, 1, 7, 2,
    0, 0, 0, 0, 8, 9, 2, 6, 0,
    7, 8, 2, 6, 4, 1, 0, 0, 5,
    0, 1, 0, 0, 0, 0, 7, 0, 8
  ]
  solution_1 = [
    5, 2, 8, 4, 6, 7, 3, 1, 9,
    9, 6, 3, 8, 1, 5, 4, 2, 7,
    1, 7, 4, 2, 9, 3, 5, 8, 6,
    2, 3, 1, 9, 7, 6, 8, 5, 4,
    8, 5, 7, 1, 2, 4, 6, 9, 3,
    4, 9, 6, 3, 5, 8, 1, 7, 2,
    3, 4, 5, 7, 8, 9, 2, 6, 1, 
    7, 8, 2, 6, 4, 1, 9, 3, 5,
    6, 1, 9, 5, 3, 2, 7, 4, 8
  ]

  puzzle_2 = [
    0, 0, 0, 2, 6, 0, 7, 0, 1,
    6, 8, 0, 0, 7, 0, 0, 9, 0,
    1, 9, 0, 0, 0, 4, 5, 0, 0,
    8, 2, 0, 1, 0, 0, 0, 4, 0,
    0, 0, 4, 6, 0, 2, 9, 0, 0,
    0, 5, 0, 0, 0, 3, 0, 2, 8,
    0, 0, 9, 3, 0, 0, 0, 7, 4,
    0, 4, 0, 0, 5, 0, 0, 3, 6,
    7, 0, 3, 0, 1, 8, 0, 0, 0
  ]

  solution_2 = [
    4, 3, 5, 2, 6, 9, 7, 8, 1,
    6, 8, 2, 5, 7, 1, 4, 9, 3,
    1, 9, 7, 8, 3, 4, 5, 6, 2,
    8, 2, 6, 1, 9, 5, 3, 4, 7,
    3, 7, 4, 6, 8, 2, 9, 1, 5,
    9, 5, 1, 7, 4, 3, 6, 2, 8,
    5, 1, 9, 3, 2, 6, 8, 7, 4,
    2, 4, 8, 9, 5, 7, 1, 3, 6,
    7, 6, 3, 4, 1, 8, 2, 5, 9,
  ]

  def test_solve_sudoku_puzzle(self):
    # self.assertEqual(solve_sudoku_puzzle(self.puzzle_1), self.solution_1)
    self.assertEqual(solve_sudoku_puzzle(self.puzzle_2), self.solution_2)

if __name__ == "__main__":
  unittest.main()