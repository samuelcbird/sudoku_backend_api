class Iterator:
  def __init__(self, start_at: int = 0):
    self._current_iteration: int = start_at
    self._previous_iteration: int = 0
    self._has_been_negative: bool = False

  def _setPreviousIteration(self, to: int):
    self._previous_iteration = to

  def incrementOne(self):
    self._setPreviousIteration(self._current_iteration)
    self._current_iteration += 1

  def decrementOne(self):
    self._setPreviousIteration(self._current_iteration)

    if (self._current_iteration - 1) < 0:
      self._has_been_negative = True
    
    self._current_iteration -= 1

  def getCurrentIteration(self) -> int:
    return self._current_iteration

  def getPreviousIteration(self) -> int:
    return self._previous_iteration

  def hasBeenNegative(self) -> bool:
    return self._has_been_negative