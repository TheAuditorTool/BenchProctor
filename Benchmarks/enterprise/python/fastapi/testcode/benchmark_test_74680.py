# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


def relay_value(value):
    return value

async def BenchmarkTest74680(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HTMLResponse(Template(processed).render())
