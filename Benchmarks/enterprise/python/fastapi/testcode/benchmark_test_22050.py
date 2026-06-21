# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest22050(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
