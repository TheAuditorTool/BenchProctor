# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import os
from starlette.responses import JSONResponse
import json


async def BenchmarkTest54763(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
