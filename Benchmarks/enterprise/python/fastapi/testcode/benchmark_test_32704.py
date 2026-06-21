# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest32704(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
