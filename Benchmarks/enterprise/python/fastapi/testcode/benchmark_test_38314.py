# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest38314(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
