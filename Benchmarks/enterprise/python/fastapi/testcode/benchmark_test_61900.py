# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from fastapi import Form


async def BenchmarkTest61900(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
