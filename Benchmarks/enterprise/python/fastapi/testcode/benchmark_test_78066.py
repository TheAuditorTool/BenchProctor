# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest78066(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    return HTMLResponse('<img src="' + str(data) + '">')
