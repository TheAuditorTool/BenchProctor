# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import requests


def ensure_str(value):
    return str(value)

async def BenchmarkTest68421(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ensure_str(raw_body)
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
