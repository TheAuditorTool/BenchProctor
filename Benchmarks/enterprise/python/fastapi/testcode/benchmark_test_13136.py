# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest13136(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
