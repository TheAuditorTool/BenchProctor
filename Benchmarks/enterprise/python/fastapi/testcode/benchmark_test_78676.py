# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest78676(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    return HTMLResponse('<div>' + str(processed) + '</div>')
