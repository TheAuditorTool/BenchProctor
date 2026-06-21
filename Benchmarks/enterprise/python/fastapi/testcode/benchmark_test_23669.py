# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest23669(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
