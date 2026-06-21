# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest20246(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
