# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest06395(request: Request):
    ua_value = request.headers.get('user-agent', '')
    return HTMLResponse('<div>' + str(ua_value) + '</div>')
