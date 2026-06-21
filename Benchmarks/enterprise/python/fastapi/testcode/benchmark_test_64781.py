# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from urllib.parse import unquote


async def BenchmarkTest64781(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
