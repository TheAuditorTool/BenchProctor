# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest33042(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
