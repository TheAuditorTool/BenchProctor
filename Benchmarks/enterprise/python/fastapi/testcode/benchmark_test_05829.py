# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest05829(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
