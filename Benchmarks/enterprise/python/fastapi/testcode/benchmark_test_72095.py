# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import urllib.request
import urllib.parse
import ssl


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest72095(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
