# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


request_state: dict[str, str] = {}

async def BenchmarkTest24282(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
