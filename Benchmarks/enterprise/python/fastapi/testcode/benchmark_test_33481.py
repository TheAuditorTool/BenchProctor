# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest33481(request: Request):
    origin_value = request.headers.get('origin', '')
    return HTMLResponse(str(origin_value))
