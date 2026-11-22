# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from Crypto.Hash import SHA256
from pydantic import BaseModel
from starlette.responses import JSONResponse


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


@app.post("/BenchmarkTest00163")
async def BenchmarkTest00163(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
