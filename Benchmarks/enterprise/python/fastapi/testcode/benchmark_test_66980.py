# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest66980(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
