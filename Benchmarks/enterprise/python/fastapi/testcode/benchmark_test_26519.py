# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import base64


async def BenchmarkTest26519(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
