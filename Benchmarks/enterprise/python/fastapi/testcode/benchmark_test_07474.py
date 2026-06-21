# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest07474(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
