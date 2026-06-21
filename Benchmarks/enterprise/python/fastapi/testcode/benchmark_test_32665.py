# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest32665(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % str(header_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
