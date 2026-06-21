# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest69288(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    return HTMLResponse('<div>' + str(header_value) + '</div>')
