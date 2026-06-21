# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest74857(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
