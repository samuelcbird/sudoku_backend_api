import os
from mangum import Mangum
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from schemas.schemas import SolveRequest, HelperRequest, SolveResponse, HelperResponse
from logic.solution import Solution

app = FastAPI(title="SudokuSolverAPI")

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_methods=['POST'],
)

app.mount("/static", StaticFiles(directory="public/favicon_package"), name="static")

@app.get('/')
async def root():
  return FileResponse("public/index.html")

@app.post('/solve', response_model=SolveResponse)
async def solve(request: SolveRequest):
  try:
    solver = Solution(request.puzzle)
    solution: list[int] = solver.full_solution()
    headers = { "Access-Control-Allow-Origin": "*" }
    response = { 'input': request.puzzle, 'solution': solution }
    return JSONResponse(content=response, headers=headers)
  except Exception as E:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(E))

  
@app.post('/help', response_model=HelperResponse)
async def help(request: HelperRequest):
  try:
    solver = Solution(request.unsolved_puzzle, request.attempted_puzzle)
    incorrect_indexes: list[int] = solver.show_incorrect_answers()
    headers = { "Access-Control-Allow-Origin": "*" }
    response = { 'attempted_puzzle': request.attempted_puzzle, 'incorrect_indexes': incorrect_indexes }
    return JSONResponse(content=response, headers=headers)
  except Exception as E:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(E))


handler = Mangum(app)
