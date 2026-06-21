# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest51495(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
