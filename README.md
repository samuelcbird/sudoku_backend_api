# Sudoku Solver API

My inspirations for this project included:

- Create my first backend service and API.
- Build a sudoku solver that worked how it is supposed to (my original one was riddled with problems).
- Implement input validation and error handling.
- Deploy a service on AWS Lambda.

Take a look at the documentation [here](https://ivsmep72heftu676jlpmbr27va0wwvid.lambda-url.eu-west-1.on.aws/).

## Stack

- Python
- FastAPI
- Uvicorn
- Mangum
- Serverless

## Endpoints

See the [documentation](https://ivsmep72heftu676jlpmbr27va0wwvid.lambda-url.eu-west-1.on.aws/) for schemas and full details. 

### /solve

Exactly as you'd expect, given an empty puzzle as input, it returns the solved puzzle.

### /help

Given an empty puzzle, and a attempted solution (finished or half-finished) of that puzzle, it will return where you've gone wrong. 

## Future updates

I have other projects I'm currently working on (including a frontend app that will use this API) but hope to improve the algorithm still in the future.

## Pull Requests

Pull requests are welcome. 

