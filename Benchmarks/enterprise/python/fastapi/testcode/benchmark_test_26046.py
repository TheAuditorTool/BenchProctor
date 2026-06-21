# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
import urllib.request


@dataclass
class FormData:
    payload: str

async def BenchmarkTest26046(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
