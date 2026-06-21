# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest19719(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    return HTMLResponse('<div>' + str(data) + '</div>')
