# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


request_state: dict[str, str] = {}

async def BenchmarkTest35998(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
