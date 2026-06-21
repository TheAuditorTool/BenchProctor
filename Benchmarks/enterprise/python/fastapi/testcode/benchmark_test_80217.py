# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest80217(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
