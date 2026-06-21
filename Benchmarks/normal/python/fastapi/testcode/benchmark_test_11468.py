# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


request_state: dict[str, str] = {}

async def BenchmarkTest11468(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
