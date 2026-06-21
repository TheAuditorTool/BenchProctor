# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest06764(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse(Template(data).render())
    return {"updated": True}
