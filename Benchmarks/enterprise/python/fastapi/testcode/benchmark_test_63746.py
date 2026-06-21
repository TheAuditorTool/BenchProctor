# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest63746(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    return HTMLResponse(str(data))
