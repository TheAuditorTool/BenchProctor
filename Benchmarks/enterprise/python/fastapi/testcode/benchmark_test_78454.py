# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse


async def BenchmarkTest78454(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = xml_value
    return HTMLResponse(Template(processed).render())
