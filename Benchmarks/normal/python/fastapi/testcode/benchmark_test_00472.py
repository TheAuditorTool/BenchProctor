# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest00472(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
