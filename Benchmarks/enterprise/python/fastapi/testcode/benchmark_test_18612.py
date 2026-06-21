# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest18612(request: Request, field: str = Form('')):
    field_value = field
    return HTMLResponse('<html><body><h1>' + str(field_value) + '</h1></body></html>')
