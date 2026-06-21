# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest44118(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
