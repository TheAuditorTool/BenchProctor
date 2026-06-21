# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest01473(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
