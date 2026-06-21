# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from types import SimpleNamespace


async def BenchmarkTest24814(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
