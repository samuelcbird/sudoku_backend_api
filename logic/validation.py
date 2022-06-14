import logic.slicer as slicer

def check_length(func):
  def validate(*puzzles):
    for puzzle in puzzles:
      if len(puzzle) < 81 or len(puzzle) > 81:
        raise Exception('Invalid puzzle length.')

    return func(*puzzles)
  return validate

def check_amount_of_givens(func): 
  def validate(*puzzles):
    numbers_given: int = 0

    for fields in puzzles[0]:
      if fields > 0:
        numbers_given += 1

    if numbers_given < 17:
      raise Exception('Insufficient given numbers')
  
    return func(*puzzles)
  return validate
  
def check_for_duplicate_givens(func):
  def validate(*puzzles):
    if duplicate_in_row(puzzles[0]):
      raise Exception('Duplicate given in row.')
    if duplicate_in_column(puzzles[0]):
      raise Exception('Duplicate given in column.')
    if duplicate_in_box(puzzles[0]):
      raise Exception('Duplicate given in box.')
    
    return func(*puzzles)
  return validate

# some problem here... need to debug
def duplicate_in_row(puzzle: list[int]) -> bool:
  for i in range(0, 73, 9):
    slice = slicer.create_horizontal_slice(i, puzzle)
    if duplicate_in_array(slice):
      return True
  return False

def duplicate_in_column(puzzle: list[int]) -> bool:
  for i in range(0, 9):
    slice = slicer.create_vertical_slice(i, puzzle)
    if duplicate_in_array(slice):
      return True
  return False

def duplicate_in_box(puzzle: list[int]) -> bool:
  indexes: list[int] = [0, 3, 6, 27, 30, 33, 54, 57, 60]
  
  for i in indexes:
    slice = slicer.create_square_slice(i, puzzle)
    if duplicate_in_array(slice):
      return True
  return False

def duplicate_in_array(slice: list[int]) -> bool:
  for given in range(1, 10):
    if slice.count(given) > 1:
      return True
  return False
