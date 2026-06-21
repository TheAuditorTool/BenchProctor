# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest13777(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
