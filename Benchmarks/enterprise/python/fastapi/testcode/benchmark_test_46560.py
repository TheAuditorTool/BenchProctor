# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest46560(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
