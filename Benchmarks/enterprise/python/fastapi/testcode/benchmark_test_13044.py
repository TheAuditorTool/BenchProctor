# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest13044(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    return HTMLResponse('<div>' + str(data) + '</div>')
