# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest67130(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
