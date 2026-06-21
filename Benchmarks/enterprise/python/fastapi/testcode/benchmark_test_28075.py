# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest28075(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
