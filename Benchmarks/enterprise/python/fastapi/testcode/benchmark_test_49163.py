# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest49163(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
