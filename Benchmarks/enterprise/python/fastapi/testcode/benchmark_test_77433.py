# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest77433(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    processed = data[:64]
    return HTMLResponse(Template(processed).render())
