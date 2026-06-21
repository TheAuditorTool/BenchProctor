# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest57554(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
