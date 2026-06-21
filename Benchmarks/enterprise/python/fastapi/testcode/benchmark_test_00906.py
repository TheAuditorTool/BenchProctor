# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest00906(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return HTMLResponse('<div>' + str(data) + '</div>')
