# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest01563(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
