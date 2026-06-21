# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import json
from app_runtime import auth_check


async def BenchmarkTest33652(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
