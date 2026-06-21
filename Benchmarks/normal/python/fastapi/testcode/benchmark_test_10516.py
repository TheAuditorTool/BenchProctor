# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest10516(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
