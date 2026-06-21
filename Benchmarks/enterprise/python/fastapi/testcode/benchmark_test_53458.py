# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def relay_value(value):
    return value

async def BenchmarkTest53458(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
