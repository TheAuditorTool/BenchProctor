# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest24769(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
