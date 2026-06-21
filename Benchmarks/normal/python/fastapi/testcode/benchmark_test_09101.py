# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import markdown
import bleach


request_state: dict[str, str] = {}

async def BenchmarkTest09101(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    processed = bleach.clean(markdown.markdown(data))
    return HTMLResponse('<div>' + str(processed) + '</div>')
