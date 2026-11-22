# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import PlainTextResponse
from fastapi.responses import JSONResponse


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


@app.post("/BenchmarkTest00106")
async def BenchmarkTest00106(request: Request, req: UserInput):
    json_value = req.payload
    with open('/var/app/data/' + str(json_value), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
