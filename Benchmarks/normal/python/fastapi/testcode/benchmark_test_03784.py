# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest03784(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
