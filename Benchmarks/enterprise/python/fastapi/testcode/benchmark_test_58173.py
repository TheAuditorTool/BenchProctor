# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest58173(request: Request):
    origin_value = request.headers.get('origin', '')
    return HTMLResponse(Template(origin_value).render())
