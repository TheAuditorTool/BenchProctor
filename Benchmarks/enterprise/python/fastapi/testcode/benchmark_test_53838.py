# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import HTMLResponse


async def BenchmarkTest53838(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
