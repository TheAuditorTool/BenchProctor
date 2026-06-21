# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import os
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def relay_value(value):
    return value

async def BenchmarkTest07648(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
