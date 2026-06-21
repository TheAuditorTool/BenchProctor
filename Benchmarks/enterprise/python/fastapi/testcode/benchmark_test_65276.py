# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest65276(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    return HTMLResponse(str(data))
