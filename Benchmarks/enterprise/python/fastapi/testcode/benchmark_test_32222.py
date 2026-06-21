# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse


async def BenchmarkTest32222(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
