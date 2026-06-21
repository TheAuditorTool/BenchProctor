# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest44032(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    return HTMLResponse('<div>' + str(data) + '</div>')
