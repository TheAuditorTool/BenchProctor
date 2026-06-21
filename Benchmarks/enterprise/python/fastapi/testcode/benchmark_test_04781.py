# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest04781(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return HTMLResponse('<div>' + str(data) + '</div>')
