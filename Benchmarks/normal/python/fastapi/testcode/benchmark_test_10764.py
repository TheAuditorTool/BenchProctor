# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest10764(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(data)})
