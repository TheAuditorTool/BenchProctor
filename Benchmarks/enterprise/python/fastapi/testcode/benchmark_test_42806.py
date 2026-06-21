# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest42806(request: Request):
    referer_value = request.headers.get('referer', '')
    return HTMLResponse(str(referer_value))
