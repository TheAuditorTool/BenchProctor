# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest73297(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    async def _evasion_task():
        return HTMLResponse(Template(data).render())
    return await _evasion_task()
