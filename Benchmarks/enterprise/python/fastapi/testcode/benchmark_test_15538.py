# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest15538(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    return HTMLResponse(Template(data).render())
