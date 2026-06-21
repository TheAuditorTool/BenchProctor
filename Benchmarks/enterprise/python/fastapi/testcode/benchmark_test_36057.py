# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest36057(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
