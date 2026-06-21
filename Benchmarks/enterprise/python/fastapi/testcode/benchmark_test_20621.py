# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import time
import runpy


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest20621(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    if time.time() > 1000000000:
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
