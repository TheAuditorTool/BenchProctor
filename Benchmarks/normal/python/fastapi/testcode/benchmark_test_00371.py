# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest00371(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
