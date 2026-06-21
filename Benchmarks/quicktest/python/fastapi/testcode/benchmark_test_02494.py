# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest02494(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
