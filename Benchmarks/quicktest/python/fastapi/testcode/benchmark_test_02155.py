# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


request_state: dict[str, str] = {}

async def BenchmarkTest02155(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
