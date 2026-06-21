# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest19914(request: Request):
    upload_name = (await request.form()).get('upload', '')
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    return HTMLResponse(Template(data).render())
