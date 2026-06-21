# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest44972(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
