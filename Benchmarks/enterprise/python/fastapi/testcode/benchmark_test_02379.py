# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest02379(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(data)})
