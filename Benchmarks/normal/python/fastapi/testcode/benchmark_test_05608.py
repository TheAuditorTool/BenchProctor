# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest05608(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HTMLResponse('<div>' + str(data) + '</div>')
