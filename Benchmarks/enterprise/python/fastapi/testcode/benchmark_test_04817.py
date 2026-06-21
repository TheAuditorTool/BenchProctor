# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest04817(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    return HTMLResponse(Template(data).render())
