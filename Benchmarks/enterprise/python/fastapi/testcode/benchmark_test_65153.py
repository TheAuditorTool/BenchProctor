# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import ast


async def BenchmarkTest65153(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse(Template(data).render())", '<sink>', 'exec'))
    return _ev['r']
