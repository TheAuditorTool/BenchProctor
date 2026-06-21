# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest36832(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
