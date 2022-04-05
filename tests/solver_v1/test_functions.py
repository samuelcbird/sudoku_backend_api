import unittest
from tests.solver_v1.testing_data import test_puzzles, test_slices
from solver_v1.functions import create_horizontal_slice, create_square_slice, create_vertical_slice, number_is_valid
from solver_v1.main import solve_sudoku_puzzle

class TestSolverFunctions(unittest.TestCase):

  def test_create_square_slice(self):
    self.assertEqual(create_square_slice(34, test_slices['input_1']), test_slices['square_slice'])

  def test_create_horizontal_slice(self):
    self.assertEqual(create_horizontal_slice(34, test_slices['input_1']), test_slices['horiz_slice'])

  def test_create_vertical_slice(self):
    self.assertEqual(create_vertical_slice(34, test_slices['input_1']), test_slices['vert_slice'])

  def test_number_is_valid(self):
    self.assertTrue(number_is_valid(68, test_slices['input_1']))
    self.assertFalse(number_is_valid(64, test_slices['input_1']))

  def test_solve_sudoku_puzzle(self):
    self.assertEqual(solve_sudoku_puzzle(test_puzzles['puzzle_1']), test_puzzles['solution_1']) # pass
    self.assertEqual(solve_sudoku_puzzle(test_puzzles['puzzle_2']), test_puzzles['solution_2']) # pass
    self.assertEqual(solve_sudoku_puzzle(test_puzzles['puzzle_3']), test_puzzles['solution_3']) # pass
    self.assertEqual(solve_sudoku_puzzle(test_puzzles['puzzle_4']), test_puzzles['solution_4']) # pass


if __name__ == "__main__":
  unittest.main()