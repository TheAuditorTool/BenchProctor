# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest42407(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
