# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


async def BenchmarkTest16602(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
