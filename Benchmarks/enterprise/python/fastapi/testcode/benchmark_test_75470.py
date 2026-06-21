# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest75470(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
