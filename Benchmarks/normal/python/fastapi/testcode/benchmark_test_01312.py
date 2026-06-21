# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest01312(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    return HTMLResponse('<div>' + str(data) + '</div>')
