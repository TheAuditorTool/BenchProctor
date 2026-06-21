# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest24124(request: Request):
    referer_value = request.headers.get('referer', '')
    return HTMLResponse('<div>' + str(referer_value) + '</div>')
