# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest28823(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    processed = html.escape(cookie_value)
    return HTMLResponse('<div>' + str(processed) + '</div>')
