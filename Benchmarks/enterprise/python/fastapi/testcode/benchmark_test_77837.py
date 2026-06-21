# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest77837(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse(Template(data).render())
    return {"updated": True}
