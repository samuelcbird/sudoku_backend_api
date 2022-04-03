import unittest
from solver_v1.functions import create_horizontal_slice, create_square_slice, create_vertical_slice, number_is_valid

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

if __name__ == "__main__":
  unittest.main()