def check_length(func):
  def validate(*inputs):
    for input in inputs:
      if len(input) < 81 or len(input) > 81:
        raise Exception('Invalid puzzle length.')
    func(*inputs)
  return validate

def check_givens(func): # needs testing / debugging
  def validate(*inputs):
    givens: int

    for number in input[0]:
      if number > 0:
        givens += 1

    if len(givens) < 17:
      raise Exception("Insufficient Givens")
    
    func(*inputs)
  return validate
