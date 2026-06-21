# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import subprocess


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest07415(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    eval(compile("subprocess.run([str(data), '--status'], shell=False)", '<sink>', 'exec'))
    return {"updated": True}
