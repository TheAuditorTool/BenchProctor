# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def relay_value(value):
    return value

async def BenchmarkTest01456(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = relay_value(ua_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
