# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


async def BenchmarkTest66503(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(header_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = header_value
    return HTMLResponse(Template(processed).render())
