# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


async def BenchmarkTest33707(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    processed = bleach.clean(forwarded_ip)
    return HTMLResponse('<div>' + str(processed) + '</div>')
