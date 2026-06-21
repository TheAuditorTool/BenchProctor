# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest36580(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
