import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from helper.main import helper
from solver_v1.main import backtracker
from solver_v2.main import solver_v2

# Schema for posting a puzzle to be solved
class SolveRequest(BaseModel):
  puzzle: list[int]

# response
class SolveResponse(BaseModel):
  input: list[int]
  solution: list[int]

class HelperResponse(BaseModel):
  input: list[int]
  incorrect_indexes: list[int]

app = FastAPI()


@app.get('/')
async def root():
  return FileResponse("public/index.html")

@app.post('/solve/', response_model=SolveResponse)
async def solve(request: SolveRequest, v1: bool = False):
  if not v1:
    solution: list[int] = solver_v2(request.puzzle)
    return { 'input': request.puzzle, 'solution': solution }
  else:
    solution: list[int] = backtracker(request.puzzle)
    return { 'input': request.puzzle, 'solution': solution}
  
@app.post('/help/', response_model=HelperResponse)
async def help(request: SolveRequest):
  response = helper(request.puzzle)
  return { 'input': request.puzzle, 'incorrect_indexes': response }

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)