import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from solver_v1.main import backtracker

# Schema for posting a puzzle to be solved
class SolveRequest(BaseModel):
  puzzle: list[int]

# response
class SolveResponse(BaseModel):
  input: list[int]
  solution: list[int]

app = FastAPI()


@app.get('/')
async def root():
  return FileResponse("public/index.html")

@app.post('/v1/', response_model=SolveResponse)
async def solver_v1(request: SolveRequest):
  solution: list[int] = backtracker(request.puzzle)
  return { 'input': request.puzzle, 'solution': solution }
  

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)