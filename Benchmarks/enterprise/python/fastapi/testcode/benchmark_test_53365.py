# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse


async def BenchmarkTest53365(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = ua_value
    return HTMLResponse(Template(processed).render())
