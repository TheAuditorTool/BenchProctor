# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest37675(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HTMLResponse(Template(processed).render())
