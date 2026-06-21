# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest40594(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
