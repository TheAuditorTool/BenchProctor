# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest05173(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
