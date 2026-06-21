# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import ast


async def BenchmarkTest61919(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    processed = data[:64]
    return HTMLResponse(Template(processed).render())
