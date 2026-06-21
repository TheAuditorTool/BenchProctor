# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest12470(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    return HTMLResponse('<img src="' + str(data) + '">')
