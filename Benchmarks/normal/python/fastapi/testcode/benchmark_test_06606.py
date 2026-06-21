# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest06606(request: Request):
    host_value = request.headers.get('host', '')
    return HTMLResponse('<div>' + str(host_value) + '</div>')
