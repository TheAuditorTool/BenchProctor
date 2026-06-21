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

async def BenchmarkTest40248(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    processed = data[:64]
    return HTMLResponse(Template(processed).render())
