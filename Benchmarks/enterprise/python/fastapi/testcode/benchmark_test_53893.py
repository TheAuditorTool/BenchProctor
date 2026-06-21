# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest53893(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
