# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest37823(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
