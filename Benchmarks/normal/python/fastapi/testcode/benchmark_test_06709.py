# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest06709(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    return HTMLResponse(str(data))
