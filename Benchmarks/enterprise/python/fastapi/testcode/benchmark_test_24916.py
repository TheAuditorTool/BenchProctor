# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest24916(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    return HTMLResponse(Template(raw_body).render())
