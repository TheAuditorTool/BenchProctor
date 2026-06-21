# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest81264(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parsed = urlparse(header_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = header_value
    requests.get(str(target_url))
    return {"updated": True}
