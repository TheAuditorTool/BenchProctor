# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest33599(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    return HTMLResponse('<div>' + str(data) + '</div>')
