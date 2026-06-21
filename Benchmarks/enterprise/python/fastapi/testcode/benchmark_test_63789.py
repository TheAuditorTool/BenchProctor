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

async def BenchmarkTest63789(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
