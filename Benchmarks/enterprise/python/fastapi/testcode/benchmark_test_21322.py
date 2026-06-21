# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest21322(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
