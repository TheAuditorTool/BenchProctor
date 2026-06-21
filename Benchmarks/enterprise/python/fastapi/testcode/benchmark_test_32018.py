# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest32018(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % str(ua_value)
    return HTMLResponse(Template(data).render())
