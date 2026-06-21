# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest20905(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    return HTMLResponse('<div>' + str(forwarded_ip) + '</div>')
