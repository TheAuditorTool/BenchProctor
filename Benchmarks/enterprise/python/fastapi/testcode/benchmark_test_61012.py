# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def relay_value(value):
    return value

async def BenchmarkTest61012(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
