# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from urllib.parse import unquote


async def BenchmarkTest51872(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
