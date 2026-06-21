# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest09811(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    return HTMLResponse('<div>' + str(data) + '</div>')
