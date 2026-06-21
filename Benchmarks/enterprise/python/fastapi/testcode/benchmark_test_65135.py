# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest65135(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    return HTMLResponse(Template(data).render())
