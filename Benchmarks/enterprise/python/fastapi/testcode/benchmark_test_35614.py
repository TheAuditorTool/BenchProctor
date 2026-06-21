# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os


def relay_value(value):
    return value

async def BenchmarkTest35614(request: Request):
    origin_value = request.headers.get('origin', '')
    data = relay_value(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse(Template(data).render())
    return {"updated": True}
