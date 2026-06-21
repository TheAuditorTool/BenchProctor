# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from fastapi import Form


async def BenchmarkTest03708(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
