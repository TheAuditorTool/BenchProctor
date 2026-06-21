# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest45676(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
