# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest50283(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if str(forwarded_ip) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
