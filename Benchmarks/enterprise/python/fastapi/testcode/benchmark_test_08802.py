# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest08802(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
