# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest33658(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    return HTMLResponse('<img src="' + str(data) + '">')
