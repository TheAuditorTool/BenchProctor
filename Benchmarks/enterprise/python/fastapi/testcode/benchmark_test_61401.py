# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest61401(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    return HTMLResponse('<div>' + str(data) + '</div>')
