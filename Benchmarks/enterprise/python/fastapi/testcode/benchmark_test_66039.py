# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest66039(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    return HTMLResponse(Template(data).render())
