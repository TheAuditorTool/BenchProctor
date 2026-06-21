# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse


async def BenchmarkTest70531(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = cookie_value
    return HTMLResponse(Template(processed).render())
