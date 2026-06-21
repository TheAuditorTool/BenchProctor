# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest44913(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
