# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest41894(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
