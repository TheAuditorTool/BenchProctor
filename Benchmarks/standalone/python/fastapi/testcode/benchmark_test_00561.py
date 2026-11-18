# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


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


@app.post("/BenchmarkTest00561")
async def BenchmarkTest00561(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
