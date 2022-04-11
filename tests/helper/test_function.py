from ast import Eq
import unittest
from helper.main import helper
from tests.solver_v1.testing_data import test_helper_puzzles

class TestHelper(unittest.TestCase):

  def test_helper(self):
    self.assertEqual(helper(test_helper_puzzles['puzzle_1']), test_helper_puzzles['response_1'])
    