# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
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

async def BenchmarkTest05347(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
