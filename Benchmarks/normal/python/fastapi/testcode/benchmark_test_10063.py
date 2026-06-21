# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest10063(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(env_value), secure=True, httponly=True, samesite='Strict')
    return resp
