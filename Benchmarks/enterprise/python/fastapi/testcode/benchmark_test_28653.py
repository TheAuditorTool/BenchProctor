# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


request_state: dict[str, str] = {}

async def BenchmarkTest28653(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
