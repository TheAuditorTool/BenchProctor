# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12352(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
