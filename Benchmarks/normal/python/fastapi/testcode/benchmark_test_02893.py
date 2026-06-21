# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest02893(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    return HTMLResponse(Template(data).render())
