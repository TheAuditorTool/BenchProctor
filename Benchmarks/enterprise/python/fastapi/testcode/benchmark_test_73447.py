# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest73447(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    return HTMLResponse('<script src="' + str(target_url) + '"></script>')
