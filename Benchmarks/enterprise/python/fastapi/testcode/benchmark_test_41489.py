# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest41489(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
