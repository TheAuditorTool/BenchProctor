# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest59977(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = coalesce_blank(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse(Template(data).render())
    return {"updated": True}
