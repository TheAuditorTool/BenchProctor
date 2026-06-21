# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import requests


def to_text(value):
    return str(value).strip()

async def BenchmarkTest26468(request: Request):
    host_value = request.headers.get('host', '')
    data = to_text(host_value)
    if str(data).lower() not in ('true', 'false'):
        return JSONResponse({'error': 'invalid boolean'}, status_code=400)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
