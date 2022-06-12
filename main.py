import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from logic.solution import Solution


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
  try:
    solver = Solution(request.puzzle)
    solution: list[int] = solver.full_solution()
    response = { 'input': request.puzzle, 'solution': solution }
    return JSONResponse(content=response)
  except Exception as E:
    raise HTTPException(status_code=400, detail='Bad request.')

  
@app.post('/help/', response_model=HelperResponse)
async def help(request: HelperRequest):
  solver = Solution(request.unsolved_puzzle, request.attempted_puzzle)
  incorrect_indexes: list[int] = solver.show_incorrect_answers()
  response = { 'attempted_puzzle': request.attempted_puzzle, 'incorrect_indexes': incorrect_indexes }

  return JSONResponse(content=response)


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
