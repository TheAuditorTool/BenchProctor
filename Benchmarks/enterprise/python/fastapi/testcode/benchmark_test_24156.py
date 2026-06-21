# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest24156(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
