# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import random
from dataclasses import dataclass
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00144")
async def BenchmarkTest00144(request: Request, req: UserInput):
    json_value = req.payload
    form = FormData(payload=json_value)
    data = form.payload
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JSONResponse({'token': str(token)}, status_code=200)
