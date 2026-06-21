# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest29169(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    processed = data[:64]
    return HTMLResponse(Template(processed).render())
