# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest53234(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
