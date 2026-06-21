# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest03677(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    globals()['counter'] = int(processed)
    return {"updated": True}
