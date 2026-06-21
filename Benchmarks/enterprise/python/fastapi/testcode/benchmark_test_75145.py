# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest75145(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
