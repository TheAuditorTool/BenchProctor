# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest23413(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HTMLResponse('<div>' + str(data) + '</div>')
