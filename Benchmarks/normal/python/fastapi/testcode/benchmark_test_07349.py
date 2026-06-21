# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest07349(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
