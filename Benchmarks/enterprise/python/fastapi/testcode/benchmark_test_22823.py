# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest22823(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
