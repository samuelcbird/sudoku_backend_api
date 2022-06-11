import unittest
from tests.solver_v1.testing_data import test_puzzles, test_slices
from logic.solution import Solution

class SolutionTests(unittest.TestCase):

  def test_figure_absolutes(self):
    solution = Solution(test_puzzles['puzzle_2'])
    self.assertEqual(solution._figure_absolutes(test_puzzles['puzzle_2']), test_puzzles['solution_2_absolutes'])

  def test_number_is_valid(self):
    validity = Solution(test_slices['input_1'])
    self.assertTrue(validity._number_is_valid(68, test_slices['input_1']))