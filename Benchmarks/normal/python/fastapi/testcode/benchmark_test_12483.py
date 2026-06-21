# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest12483(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
