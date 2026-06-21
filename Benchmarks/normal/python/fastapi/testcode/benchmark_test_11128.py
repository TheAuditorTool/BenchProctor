# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest11128(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return HTMLResponse(Template(data).render())
