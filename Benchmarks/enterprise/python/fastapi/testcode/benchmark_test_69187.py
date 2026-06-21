# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest69187(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
