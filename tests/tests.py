import unittest
from tests.solver_v1.testing_data import test_puzzles, test_slices
from logic.solution import Solution

class SolutionTests(unittest.TestCase):

  def test_figure_absolutes(self):
    puzzle_2_input: list[int] = test_puzzles['puzzle_2']
    solution_2_absolutes: list[int] = test_puzzles['solution_2_absolutes']

    solution = Solution(puzzle_2_input)
    self.assertEqual(solution._figure_absolutes(puzzle_2_input), solution_2_absolutes)

  def test_number_is_valid(self):
    sliceable_sudoku: list[int] = test_slices['input_1']
    
    solution = Solution(sliceable_sudoku)
    self.assertTrue(solution._number_is_valid(68, sliceable_sudoku))
    # self.assertFalse(solution._number_is_valid(64, sliceable_sudoku))

  def test_square_slice(self):
    sliceable_sudoku: list[int] = test_slices['input_1']
    square_slice_answer: list[int] = test_slices['square_slice']

    solution = Solution(sliceable_sudoku)
    self.assertEqual(solution._create_square_slice(34, sliceable_sudoku), square_slice_answer)

  def test_horizontal_slice(self):
    sliceable_sudoku: list[int] = test_slices['input_1']
    horiz_slice_answer: list[int] = test_slices['horiz_slice']

    solution = Solution(sliceable_sudoku)
    self.assertEqual(solution._create_horizontal_slice(34, sliceable_sudoku), horiz_slice_answer)

  def test_vertical_slice(self):
    sliceable_sudoku: list[int] = test_slices['input_1']
    vert_slice_answer: list[int] = test_slices['vert_slice']

    solution = Solution(sliceable_sudoku)
    self.assertEqual(solution._create_vertical_slice(34, sliceable_sudoku), vert_slice_answer)
  
  def test_full_solution(self):
    puzzle_1 = test_puzzles['puzzle_1']
    solution_1 = test_puzzles['solution_1']
  
    solution = Solution(puzzle_1)
    self.assertEqual(solution.full_solution(), solution_1)