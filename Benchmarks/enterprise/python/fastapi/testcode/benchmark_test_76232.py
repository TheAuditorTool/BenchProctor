# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import socket


async def BenchmarkTest76232(request: Request):
    referer_value = request.headers.get('referer', '')
    parsed = urlparse(referer_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = referer_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
