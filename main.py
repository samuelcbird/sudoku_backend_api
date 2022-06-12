from hashlib import new
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from logic.solution import Solution

from helper.main import helper
# DEPRECATED
# from solver_v1.main import backtracker
# from solver_v2.main import solver_v2

# Schema for posting a puzzle to be solved
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

app = FastAPI()

app.mount("/static", StaticFiles(directory="public/favicon_package"), name="static")

@app.get('/')
async def root():
  return FileResponse("public/index.html")

@app.post('/solve/', response_model=SolveResponse)
async def solve(request: SolveRequest):
  solver = Solution(request.puzzle)
  solution: list[int] = solver.full_solution()
  response = { 'input': request.puzzle, 'solution': solution }

  # DEPRECATED
  # solution: list[int] = solver_v2(request.puzzle)
  # response = { 'input': request.puzzle, 'solution': solution }

  return JSONResponse(content=response)
  
@app.post('/help/', response_model=HelperResponse)
async def help(request: HelperRequest):
  # DEPRECATED
  incorrect_indexes = helper(request.unsolved_puzzle, request.attempted_puzzle)
  response = { 'attempted_puzzle': request.attempted_puzzle, 'incorrect_indexes': incorrect_indexes }
  return JSONResponse(content=response)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
