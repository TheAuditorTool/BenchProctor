# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest48493(request: Request):
    origin_value = request.headers.get('origin', '')
    return HTMLResponse('<html><body><h1>' + str(origin_value) + '</h1></body></html>')
