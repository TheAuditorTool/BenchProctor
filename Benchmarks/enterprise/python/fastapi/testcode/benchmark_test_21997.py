# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest21997(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
