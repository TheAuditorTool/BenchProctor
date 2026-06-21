# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest56034(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
