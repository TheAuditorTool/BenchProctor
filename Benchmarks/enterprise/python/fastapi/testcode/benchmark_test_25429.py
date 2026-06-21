# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import urlparse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest25429(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(target_url)})
