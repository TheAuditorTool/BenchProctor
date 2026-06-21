# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest36609(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    return HTMLResponse(str(data))
