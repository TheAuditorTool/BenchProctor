# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest75351(request: Request):
    auth_header = request.headers.get('authorization', '')
    parsed = urlparse(auth_header)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = auth_header
    requests.get(str(target_url))
    return {"updated": True}
