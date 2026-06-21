# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import os
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest59774(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
