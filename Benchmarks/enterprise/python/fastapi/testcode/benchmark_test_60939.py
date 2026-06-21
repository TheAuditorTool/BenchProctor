# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest60939(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
