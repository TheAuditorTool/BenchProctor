# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest27928(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    return HTMLResponse(Template(xml_value).render())
