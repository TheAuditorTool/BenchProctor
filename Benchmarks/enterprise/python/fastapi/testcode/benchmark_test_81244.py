# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest81244(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
