# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest09362(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
