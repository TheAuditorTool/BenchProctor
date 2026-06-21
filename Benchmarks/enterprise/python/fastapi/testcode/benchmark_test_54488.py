# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest54488(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return HTMLResponse('<div>' + str(data) + '</div>')
