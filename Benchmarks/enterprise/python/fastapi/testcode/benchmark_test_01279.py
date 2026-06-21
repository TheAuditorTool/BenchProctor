# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest01279(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    def _primary():
        return HTMLResponse(Template(data).render())
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
