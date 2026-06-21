# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest53870(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': origin})
    return {"updated": True}
