# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest75713(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return {"updated": True}
