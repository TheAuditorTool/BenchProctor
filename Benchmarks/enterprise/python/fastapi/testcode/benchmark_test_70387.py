# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest70387(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
