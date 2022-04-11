import unittest
from helper.main import helper
from tests.solver_v1.testing_data import test_helper_puzzles, test_puzzles

class TestHelper(unittest.TestCase):

  def test_helper(self):
    self.assertEqual(helper(test_puzzles['puzzle_1'], test_helper_puzzles['puzzle_1']), test_helper_puzzles['response_1'])
    self.assertEqual(helper(test_puzzles['puzzle_2'], test_helper_puzzles['puzzle_2']), test_helper_puzzles['response_2'])

if __name__ == "__main__":
  unittest.main()
    