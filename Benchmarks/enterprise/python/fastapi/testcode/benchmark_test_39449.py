# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest39449(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
