# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest03653(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
