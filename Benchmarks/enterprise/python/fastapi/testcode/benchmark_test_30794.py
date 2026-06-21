# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest30794(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
