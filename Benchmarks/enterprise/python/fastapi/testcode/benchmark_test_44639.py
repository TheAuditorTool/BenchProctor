# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest44639(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
