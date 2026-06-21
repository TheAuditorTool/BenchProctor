# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import ast


async def BenchmarkTest50062(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    def _primary():
        return HTMLResponse(Template(data).render())
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
