# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import base64


async def BenchmarkTest17718(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
