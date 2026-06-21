# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest74848(request: Request):
    referer_value = request.headers.get('referer', '')
    processed = html.escape(referer_value)
    return HTMLResponse('<div>' + str(processed) + '</div>')
