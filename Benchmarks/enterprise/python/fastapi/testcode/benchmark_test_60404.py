# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import time


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest60404(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
