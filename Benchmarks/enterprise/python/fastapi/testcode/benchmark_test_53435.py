# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest53435(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    return HTMLResponse('<div>' + str(data) + '</div>')
