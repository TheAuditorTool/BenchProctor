# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest05544(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parsed = urlparse(raw_body)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = raw_body
    requests.get(str(target_url))
    return {"updated": True}
