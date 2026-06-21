# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest67455(request: Request):
    path_value = request.path_params.get('id', '')
    return HTMLResponse(Template(path_value).render())
