# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from urllib.parse import unquote


async def BenchmarkTest01076(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
