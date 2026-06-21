# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from fastapi import Form


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest60719(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
