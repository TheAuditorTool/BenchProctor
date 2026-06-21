# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest04887(request: Request):
    auth_header = request.headers.get('authorization', '')
    return HTMLResponse('<div>' + str(auth_header) + '</div>')
