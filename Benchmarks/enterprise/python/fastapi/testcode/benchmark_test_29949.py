# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest29949(request: Request):
    ua_value = request.headers.get('user-agent', '')
    processed = html.escape(ua_value)
    return HTMLResponse('<div>' + str(processed) + '</div>')
