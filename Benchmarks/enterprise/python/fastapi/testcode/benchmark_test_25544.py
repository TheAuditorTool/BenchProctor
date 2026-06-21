# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import base64


async def BenchmarkTest25544(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
