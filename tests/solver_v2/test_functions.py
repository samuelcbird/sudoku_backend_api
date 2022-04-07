import unittest
from tests.solver_v1.testing_data import test_puzzles
from solver_v2.functions import figure_absolutes
from solver_v2.main import solver_v2


class TestSolverV2Functions(unittest.TestCase):

  def test_solver_v2(self):
    self.assertEqual(figure_absolutes(test_puzzles['puzzle_1']), test_puzzles['solution_1']) 


if __name__ == "__main__":
  unittest.main()