# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest47924(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    if str(data) in ('localhost', 'internal-gateway'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
