# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


async def BenchmarkTest41301(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = cookie_value
    return HTMLResponse(Template(processed).render())
