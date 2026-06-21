# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def relay_value(value):
    return value

async def BenchmarkTest05014(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    processed = data[:64]
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
