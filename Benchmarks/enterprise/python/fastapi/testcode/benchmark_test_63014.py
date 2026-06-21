# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
import urllib.request


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest63014(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
