# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest79456(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return {"updated": True}
