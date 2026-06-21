# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest72920(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
