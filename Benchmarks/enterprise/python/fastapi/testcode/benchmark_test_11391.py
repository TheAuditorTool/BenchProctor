# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest11391(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    return HTMLResponse('<div>' + str(data) + '</div>')
