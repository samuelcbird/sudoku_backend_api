from pydantic import BaseModel

class SolveRequest(BaseModel):
  puzzle: list[int]

class HelperRequest(BaseModel):
  unsolved_puzzle: list[int]
  attempted_puzzle: list[int]

# response
class SolveResponse(BaseModel):
  input: list[int]
  solution: list[int]

class HelperResponse(BaseModel):
  attempted_puzzle: list[int]
  incorrect_indexes: list[int]