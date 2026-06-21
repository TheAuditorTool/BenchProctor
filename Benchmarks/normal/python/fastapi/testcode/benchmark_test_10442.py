# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest10442(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    async def _evasion_task():
        return HTMLResponse(Template(data).render())
    return await _evasion_task()
