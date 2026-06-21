# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import os
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest74301(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
