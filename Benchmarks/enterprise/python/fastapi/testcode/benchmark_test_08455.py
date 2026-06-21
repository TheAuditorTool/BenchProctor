# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest08455(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    return HTMLResponse(Template(data).render())
