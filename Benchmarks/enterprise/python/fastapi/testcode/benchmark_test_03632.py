# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import HTMLResponse


async def BenchmarkTest03632(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
