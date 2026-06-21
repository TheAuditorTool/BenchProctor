# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest48050(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
