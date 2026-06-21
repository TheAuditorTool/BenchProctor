# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import importlib


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest01526(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
