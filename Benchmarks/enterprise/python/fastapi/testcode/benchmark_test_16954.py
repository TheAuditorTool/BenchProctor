# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


async def BenchmarkTest16954(request: Request):
    host_value = request.headers.get('host', '')
    processed = bleach.clean(host_value)
    return HTMLResponse('<div>' + str(processed) + '</div>')
