# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest10491(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    return HTMLResponse('<div>' + str(data) + '</div>')
