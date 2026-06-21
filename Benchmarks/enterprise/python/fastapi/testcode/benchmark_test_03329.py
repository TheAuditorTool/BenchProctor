# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from urllib.parse import unquote


async def BenchmarkTest03329(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
