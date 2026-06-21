# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest00809(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
