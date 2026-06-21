# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest02550(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
