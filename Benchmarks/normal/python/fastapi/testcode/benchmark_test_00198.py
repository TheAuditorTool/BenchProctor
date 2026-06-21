# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
import ast


async def BenchmarkTest00198(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
