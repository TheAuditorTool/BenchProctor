# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest18162(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
