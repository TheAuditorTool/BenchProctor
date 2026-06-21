# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest05395(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    return HTMLResponse('<div>' + str(data) + '</div>')
