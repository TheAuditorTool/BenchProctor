# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest48088(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    return HTMLResponse(str(data))
