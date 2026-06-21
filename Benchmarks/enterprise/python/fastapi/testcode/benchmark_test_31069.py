# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest31069(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
