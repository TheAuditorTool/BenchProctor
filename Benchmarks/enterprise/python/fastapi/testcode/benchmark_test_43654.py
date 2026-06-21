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

async def BenchmarkTest43654(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
