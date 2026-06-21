# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest02990(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    return HTMLResponse('<div>' + str(data) + '</div>')
