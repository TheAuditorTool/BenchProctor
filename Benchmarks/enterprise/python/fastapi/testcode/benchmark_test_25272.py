# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest25272(request: Request):
    host_value = request.headers.get('host', '')
    processed = html.escape(host_value)
    return HTMLResponse('<div>' + str(processed) + '</div>')
