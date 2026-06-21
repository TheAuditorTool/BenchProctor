# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest07376(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    globals()['counter'] = int(processed)
    return {"updated": True}
