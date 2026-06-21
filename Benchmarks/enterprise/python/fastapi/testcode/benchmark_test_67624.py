# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest67624(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
