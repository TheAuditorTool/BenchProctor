# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import socket


async def BenchmarkTest81358(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parsed = urlparse(header_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = header_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
