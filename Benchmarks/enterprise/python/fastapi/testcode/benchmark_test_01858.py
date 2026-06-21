# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest01858(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
