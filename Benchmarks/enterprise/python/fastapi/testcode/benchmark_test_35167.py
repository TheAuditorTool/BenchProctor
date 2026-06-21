# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest35167(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    return HTMLResponse(Template(data).render())
