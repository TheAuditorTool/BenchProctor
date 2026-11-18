# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00598")
async def BenchmarkTest00598(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return JSONResponse({'error': 'not found'}, status_code=404)
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
