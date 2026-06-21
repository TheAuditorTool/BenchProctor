# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import os
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest11543(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
