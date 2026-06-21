# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest53915(request: Request):
    origin_value = request.headers.get('origin', '')
    data = default_blank(origin_value)
    def _primary():
        return HTMLResponse(Template(data).render())
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
