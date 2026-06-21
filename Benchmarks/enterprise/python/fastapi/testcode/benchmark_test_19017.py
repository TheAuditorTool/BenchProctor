# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest19017(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
