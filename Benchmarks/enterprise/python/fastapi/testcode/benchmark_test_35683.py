# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import HTMLResponse


async def BenchmarkTest35683(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    return HTMLResponse(str(data))
