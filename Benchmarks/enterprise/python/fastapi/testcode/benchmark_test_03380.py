# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest03380(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    return HTMLResponse(Template(data).render())
