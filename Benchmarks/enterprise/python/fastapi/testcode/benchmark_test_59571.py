# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest59571(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    def _primary():
        return HTMLResponse(Template(data).render())
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
