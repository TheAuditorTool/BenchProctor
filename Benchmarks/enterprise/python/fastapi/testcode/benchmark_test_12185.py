# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest12185(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
