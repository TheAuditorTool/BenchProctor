# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import time


def relay_value(value):
    return value

async def BenchmarkTest54160(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    if time.time() > 1000000000:
        return HTMLResponse(Template(data).render())
    return {"updated": True}
