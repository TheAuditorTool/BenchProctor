# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest08030(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    return HTMLResponse(str(raw_body))
