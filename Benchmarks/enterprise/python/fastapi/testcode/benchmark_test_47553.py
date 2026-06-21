# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import HTMLResponse


async def BenchmarkTest47553(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
