# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest55545(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    return HTMLResponse(Template(data).render())
