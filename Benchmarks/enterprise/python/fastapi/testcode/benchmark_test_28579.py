# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest28579(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
