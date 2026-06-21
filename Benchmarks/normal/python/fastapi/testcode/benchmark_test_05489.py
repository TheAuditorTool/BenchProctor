# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest05489(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    requests.get('https://api.pycdn.io/data', params={'q': str(target_url)}, verify=False)
    return {"updated": True}
