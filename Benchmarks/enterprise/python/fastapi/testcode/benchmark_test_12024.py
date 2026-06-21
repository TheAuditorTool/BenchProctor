# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest12024(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    return HTMLResponse('<div>' + str(data) + '</div>')
