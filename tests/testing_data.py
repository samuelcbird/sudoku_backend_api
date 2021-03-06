test_slices: dict[list[int]] = {
  'input_1': [
    0, 0, 1, 0, 0, 2, 0, 0, 3,
    0, 0, 4, 0, 0, 5, 0, 0, 6,
    0, 0, 7, 0, 0, 8, 0, 0, 9,
    0, 1, 0, 0, 1, 1, 0, 1, 2,
    0, 1, 3, 0, 1, 4, 0, 1, 5,
    0, 1, 6, 0, 1, 7, 0, 1, 8,
    0, 1, 9, 0, 2, 0, 0, 2, 1,
    0, 2, 2, 0, 2, 3, 0, 2, 4,
    0, 2, 5, 0, 2, 6, 0, 2, 7
  ],
  # expected output for input_1 with index: 34
  'square_slice': [0, 1, 2, 0, 1, 5, 0, 1, 8],
  'vert_slice': [0, 0, 0, 1, 1, 1, 2, 2, 2],
  'horiz_slice': [0, 1, 0, 0, 1, 1, 0, 1, 2]
}

test_puzzles: dict[list[int]] = {
  # from - https://www.puzzles.ca/sudoku_puzzles/sudoku_easy_1033.html
  'puzzle_1': [ # 1033 (easy)
    0, 7, 0, 0, 0, 0, 0, 0, 0,
    5, 3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 2, 0, 0, 4, 1, 0, 0, # only 9 in index:18
    0, 0, 0, 2, 0, 0, 7, 3, 0,
    8, 0, 0, 0, 0, 0, 0, 2, 6,
    0, 0, 1, 0, 0, 5, 4, 0, 0,
    3, 0, 8, 0, 0, 0, 0, 0, 0,
    6, 0, 0, 1, 0, 7, 0, 0, 3,
    0, 0, 0, 0, 0, 0, 0, 8, 0,
  ],
  'puzzle_2': [ # 1034 (easy)
    0, 5, 9, 0, 0, 0, 0, 0, 0,
    6, 0, 0, 0, 0, 0, 2, 3, 4,
    8, 0, 0, 0, 0, 6, 0, 0, 0,
    9, 0, 0, 3, 6, 0, 7, 5, 0,
    0, 0, 0, 2, 0, 0, 0, 0, 8,
    5, 0, 8, 9, 0, 7, 0, 0, 2,
    0, 6, 5, 0, 0, 0, 9, 4, 0,
    7, 0, 2, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
  ],
  # from - https://www.puzzles.ca/sudoku_puzzles/sudoku_easy_1033_solution.html
  'solution_1': [ # 1033 (easy)
    1, 7, 6, 8, 5, 2, 3, 4, 9,
    5, 3, 4, 9, 1, 6, 8, 7, 2,
    9, 8, 2, 3, 7, 4, 1, 6, 5,
    4, 6, 5, 2, 9, 8, 7, 3, 1,
    8, 9, 3, 7, 4, 1, 5, 2, 6,
    7, 2, 1, 6, 3, 5, 4, 9, 8,
    3, 5, 8, 4, 2, 9, 6, 1, 7,
    6, 4, 9, 1, 8, 7, 2, 5, 3,
    2, 1, 7, 5, 6, 3, 9, 8, 4
  ],
  'solution_2': [ # 1034 (easy)
    2, 5, 9, 4, 3, 1, 8, 7, 6,
    6, 1, 7, 8, 9, 5, 2, 3, 4,
    8, 4, 3, 7, 2, 6, 5, 1, 9,
    9, 2, 4, 3, 6, 8, 7, 5, 1,
    1, 7, 6, 2, 5, 4, 3, 9, 8,
    5, 3, 8, 9, 1, 7, 4, 6, 2,
    3, 6, 5, 1, 8, 2, 9, 4, 7,
    7, 9, 2, 6, 4, 3, 1, 8, 5,
    4, 8, 1, 5, 7, 9, 6, 2, 3,
  ],
  'solution_2_absolutes': [
    0, 5, 9, 0, 0, 0, 0, 0, 0,
    6, 0, 0, 0, 0, 0, 2, 3, 4,
    8, 0, 0, 0, 0, 6, 0, 0, 0,
    9, 2, 4, 3, 6, 8, 7, 5, 1,
    0, 0, 0, 2, 0, 0, 0, 9, 8,
    5, 0, 8, 9, 0, 7, 0, 6, 2,
    0, 6, 5, 0, 0, 0, 9, 4, 0,
    7, 0, 2, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0
  ],
  # from - https://www.puzzles.ca/sudoku_puzzles/sudoku_easy_1031.html
  'puzzle_3': [ # 1031 (easy)
    8, 0, 0, 0, 0, 2, 0, 4, 0,
    0, 7, 0, 0, 8, 0, 5, 6, 0,
    0, 5, 6, 0, 7, 0, 9, 0, 0,
    1, 0, 2, 9, 5, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 2, 7, 4,
    0, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 0, 6, 1, 5, 4, 8, 0,
    0, 0, 0, 2, 0, 0, 6, 0, 0,
  ],
  'puzzle_4': [ # 1032 (easy)
    6, 0, 0, 2, 9, 0, 0, 0, 0,
    0, 0, 5, 0, 4, 0, 0, 0, 2,
    4, 8, 0, 0, 7, 5, 9, 0, 0,
    0, 4, 0, 0, 1, 0, 0, 8, 6,
    0, 2, 0, 4, 8, 0, 5, 9, 0,
    1, 0, 0, 0, 0, 6, 0, 0, 0,
    2, 0, 0, 0, 0, 0, 7, 0, 0,
    0, 0, 7, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 5, 0, 0, 0, 4, 0,
  ],
  # from - https://www.puzzles.ca/sudoku_puzzles/sudoku_easy_1031_solution.html
  'solution_3': [ # 1031 (easy)
    8, 1, 9, 5, 6, 2, 7, 4, 3,
    4, 7, 3, 1, 8, 9, 5, 6, 2,
    2, 5, 6, 3, 7, 4, 9, 1, 8,
    1, 4, 2, 9, 5, 7, 8, 3, 6,
    7, 3, 8, 4, 2, 6, 1, 9, 5,
    6, 9, 5, 8, 3, 1, 2, 7, 4,
    5, 6, 4, 7, 9, 8, 3, 2, 1,
    3, 2, 7, 6, 1, 5, 4, 8, 9,
    9, 8, 1, 2, 4, 3, 6, 5, 7,
  ],
  'solution_4': [ # 1032 (easy)
    6, 7, 3, 2, 9, 1, 8, 5, 4,
    9, 1, 5, 3, 4, 8, 6, 7, 2,
    4, 8, 2, 6, 7, 5, 9, 1, 3,
    5, 4, 9, 7, 1, 2, 3, 8, 6,
    7, 2, 6, 4, 8, 3, 5, 9, 1,
    1, 3, 8, 9, 5, 6, 4, 2, 7,
    2, 5, 4, 1, 6, 9, 7, 3, 8,
    3, 9, 7, 8, 2, 4, 1, 6, 5,
    8, 6, 1, 5, 3, 7, 2, 4, 9
  ]
}

test_helper_puzzles: dict[list[int]] = {
  # from - https://www.puzzles.ca/sudoku_puzzles/sudoku_easy_1033.html
  'puzzle_1': [ # 1033 (easy)
    0, 7, 3, 0, 0, 0, 0, 0, 0,
    5, 3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 2, 0, 0, 4, 1, 4, 0,
    0, 0, 0, 2, 0, 0, 7, 3, 0,
    8, 0, 0, 0, 0, 0, 0, 2, 6,
    0, 0, 1, 0, 0, 5, 4, 0, 0,
    3, 0, 8, 0, 0, 0, 0, 0, 0,
    6, 0, 0, 1, 0, 7, 8, 0, 3,
    0, 0, 0, 0, 0, 0, 0, 8, 0,
  ],
  'puzzle_2': [ # 1034 (easy)
    0, 5, 9, 0, 0, 0, 0, 0, 0,
    6, 0, 0, 0, 0, 0, 2, 3, 4,
    8, 4, 3, 7, 0, 6, 0, 0, 0,
    9, 0, 0, 3, 6, 0, 7, 5, 0,
    0, 0, 0, 2, 8, 0, 0, 0, 8,
    5, 0, 8, 9, 0, 7, 0, 0, 2,
    0, 6, 5, 0, 0, 0, 9, 4, 0,
    7, 0, 2, 0, 0, 3, 6, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
  ],
  'response_1': [
    2, 25, 69
  ],
  'response_2': [
    40, 69, 70
  ]
}