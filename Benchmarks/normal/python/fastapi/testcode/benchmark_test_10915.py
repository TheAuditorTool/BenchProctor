# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest10915(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
