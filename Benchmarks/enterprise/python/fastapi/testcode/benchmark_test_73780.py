# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest73780(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
