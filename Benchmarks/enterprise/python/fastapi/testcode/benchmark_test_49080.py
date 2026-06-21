# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest49080(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
