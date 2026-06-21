# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import RedirectResponse
import urllib.parse


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest16943(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
