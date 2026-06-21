# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from fastapi import Form


async def BenchmarkTest33018(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
