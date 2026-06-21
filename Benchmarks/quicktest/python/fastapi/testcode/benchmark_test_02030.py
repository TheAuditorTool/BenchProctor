# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest02030(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
