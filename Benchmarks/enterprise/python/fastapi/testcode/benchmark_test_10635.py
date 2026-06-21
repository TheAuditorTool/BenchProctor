# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from fastapi import Form


async def BenchmarkTest10635(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
