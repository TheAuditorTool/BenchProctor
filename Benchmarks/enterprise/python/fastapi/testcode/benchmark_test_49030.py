# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest49030(request: Request):
    path_value = request.path_params.get('id', '')
    return HTMLResponse('<img src="' + str(path_value) + '">')
