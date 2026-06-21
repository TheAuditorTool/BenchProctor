# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest17908(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    return HTMLResponse(str(cookie_value))
