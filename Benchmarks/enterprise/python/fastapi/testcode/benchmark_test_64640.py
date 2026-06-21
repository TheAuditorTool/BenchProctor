# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest64640(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
