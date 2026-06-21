# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest01697(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '{}'.format(header_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
