# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest38060(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
