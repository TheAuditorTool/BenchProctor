# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest75973(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
