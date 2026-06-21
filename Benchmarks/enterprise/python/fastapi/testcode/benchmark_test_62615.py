# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest62615(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
