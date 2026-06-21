# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest64904(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
