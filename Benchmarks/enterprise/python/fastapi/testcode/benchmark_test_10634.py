# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest10634(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
