from fastapi import FastAPI
from fastapi.responses import FileResponse

from solver_v1.functions.functions import horizontal_check


app = FastAPI();


@app.get('/')
async def root():
  return FileResponse("public/index.html")

@app.get('/test')
async def horiz_test(input: int):
  result: int = await horizontal_check(input)
  return result