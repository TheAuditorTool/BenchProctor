# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest05200(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
