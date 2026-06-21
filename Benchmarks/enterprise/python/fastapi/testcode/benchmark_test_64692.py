# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form
import time


request_state: dict[str, str] = {}

async def BenchmarkTest64692(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
