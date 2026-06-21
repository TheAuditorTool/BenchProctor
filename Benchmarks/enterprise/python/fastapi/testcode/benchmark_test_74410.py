# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest74410(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
