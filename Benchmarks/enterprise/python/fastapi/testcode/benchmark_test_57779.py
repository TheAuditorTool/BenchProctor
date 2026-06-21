# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from fastapi import Form
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest57779(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return {"updated": True}
