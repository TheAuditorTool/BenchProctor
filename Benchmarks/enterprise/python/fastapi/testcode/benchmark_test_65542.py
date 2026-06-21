# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import json


request_state: dict[str, str] = {}

async def BenchmarkTest65542(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    async def _evasion_task():
        return HTMLResponse(Template(data).render())
    return await _evasion_task()
