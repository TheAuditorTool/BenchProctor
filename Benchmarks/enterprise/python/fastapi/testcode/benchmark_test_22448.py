# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import time


request_state: dict[str, str] = {}

async def BenchmarkTest22448(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    if time.time() > 1000000000:
        return HTMLResponse(Template(data).render())
    return {"updated": True}
