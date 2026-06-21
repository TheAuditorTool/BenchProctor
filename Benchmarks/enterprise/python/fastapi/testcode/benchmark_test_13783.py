# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest13783(request: Request):
    origin_value = request.headers.get('origin', '')
    parsed = urlparse(origin_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = origin_value
    return HTMLResponse('<script src="' + str(target_url) + '"></script>')
