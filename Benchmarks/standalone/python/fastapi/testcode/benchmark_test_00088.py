# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import StreamingResponse
from pydantic import BaseModel
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


@app.post("/BenchmarkTest00088")
async def BenchmarkTest00088(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    return StreamingResponse(iter(['<div>' + str(data) + '</div>']), media_type='text/html')
