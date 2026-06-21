# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest42087(request: Request):
    referer_value = request.headers.get('referer', '')
    return JSONResponse({'error': str(referer_value), 'stack': repr(locals())}, status_code=500)
