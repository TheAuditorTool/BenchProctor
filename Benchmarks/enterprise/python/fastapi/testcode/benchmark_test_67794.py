# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest67794(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    return HTMLResponse(str(forwarded_ip))
